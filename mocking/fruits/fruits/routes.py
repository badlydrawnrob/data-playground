# ------------------------------------------------------------------------------
# Routes
# ==============================================================================
# > See `badlydrawnrob/python-playground/building-with-fast-api` for more docs,
# > and coding style guides.
# 
# We're using `@fruits_router` rather than `@app` here as it's better organised.
# You need to register the router in `app.py` with `include_router`.
#
# See `fruits.models` for information on our model types.
#
#
# Coding style is a personal preference
# -------------------------------------
# > Prefer functional (occasionally objects speed up performance)
# 
# DRY is great but don't over use it: similar is not the same as identical.
# Brutalist, minimalist, zen and explicit is better than implicit.
#
# See also `app.py` "Learning frame" for coding standards.
#
#
# Routes
# ------
# > You can split out different route groups for better organisation
#
# - @ https://fastapi.tiangolo.com/tutorial/bigger-applications/
# - @ https://stackoverflow.com/a/67318405
#
#
# Requests
# --------
# > You can use named arguments with types for clarity.
# > These can be named anything you like (unless keyword arguments).
# 
# - `body` -> `data` is a more descriptive name (to me)
# - `session=Depends(get_session)` is an example of `**kwargs`
# - `FruitsModelIn` can be converted to a dictionary
#     - `**data.model_dump()` can be used inside `Fruits` table instance
#     - `exclude_unset=True` removes any `None` values in the dictionary
#
#
# Responses
# ---------
# > See "APIs You Won't Hate" (book 2) for return values and error guides.
#
# 1. Hide any sensitive values (primary key hidden by default)
# 2. If SQL return is a singleton, use `.first()` where possible
# 3. ⚠️ SQLite 3.35.0 and above supports the returning clause (this is non-optional)
#     - Removes the need for read/writes and changing transaction type
#     - If a query supports returning values and we don't use it, we can't
#       check if any rows were updated! (See `update_fruit` as an example)
#
#
# ⛔️ API Errors and bugs
# ----------------------
# > See `README.md` of `badlydrawnrob/python-playground/building-with-fast-api/
# 
# For a list of expected errors with APIs!
#
#
# ------------------------------------------------------------------------------
# WISHLIST
# ------------------------------------------------------------------------------
# 1. Create a filter, pagination, and search route?
#    - ⭐️ Probably a good time to use RAW sql queries
#    - Investigate `case` in Python` to validate query strings
#    - @ https://stackoverflow.com/a/11479840 (Python 3.10+)
# 2. Understand and implement the `BaseUser` table properly
#    - And how does it differ from `piccolo_user` table?
#    - @ https://github.com/sinisaos/simple-piccolo/blob/main/fastapi_app.py#L73
#    - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/authentication/baseuser.html#baseuser
#    - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/authentication/baseuser.html#extending-baseuser
# 3. Create custom Pydantic types for joins (rather than `create_pydantic_model`)
#    - The more complex the join, the harder it is for Piccolo "magic"!
# 4. Protect against XSS injections (ask Mike)
#    - Mostly needed when rich text or javascript is a possiblity
# 5. Harden validating fields and routes ...
#    - Fields are not empty and not null, for example
#    - SQLite errors such as `UNIQUE` constraints
# 6. Write an endpoint to get basic user preferences
#    - You'd grab this after getting the JWT with Elm Lang
# 7. Transactions: understand when to be careful with `select()` then writes
# 8. Can UUID be `None` in the Pydantic model if it's auto-generated? (see `FruitsModelIn`)
#
#
# Questions
# ---------
# 1. When do queries not return an `[]` empty list?
# 2. How to assure a singleton query is indeed unique?
# 3. `Depends()` can go in the route decorator AND route function?

from auth.authenticate import authenticate
from auth.jwt_handler import create_access_token

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from fruits.models import FruitsModelIn, FruitsAllModelOut, FruitsModelOut, TokenResponse
from fruits.tables import Fruits, Colors

from piccolo.apps.user.tables import BaseUser

from typing import List


fruits_router = APIRouter(
    tags=["Fruits"] # used for `/redoc` (menu groupings)
)

user_router = APIRouter(
    tags=["User"]
)

# ------------------------------------------------------------------------------
# User operations
# ==============================================================================
# > For now the core arguments are needed, but you may wish to add `client_id`
# > and `client_secret` to your API (currently set to `none` for testing)
#
# @ https://www.oauth.com/oauth2-servers/client-registration/client-id-secret/

@user_router.post("/login") #! (2)
async def sign_in_user(
        data: OAuth2PasswordRequestForm = Depends()
    ) -> TokenResponse:

    user = await BaseUser.login(
        username=data.username,
        password=data.password
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User doesn't exist or invalid password"
        )

    access_token = create_access_token(data.username)

    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }


# ------------------------------------------------------------------------------
# Read operations
# ==============================================================================
# > ⚠️ Response type is generally redundant if using `response_model=`, but if
# > both are used `response_model=` takes precedence.

@fruits_router.get(
        "/",
        response_model=List[FruitsAllModelOut],
        # dependencies=[Depends(transaction)]
        )
async def retrieve_all_fruits():
    """Return all fruits

    I've removed the response type from the function, as we're using the
    `response_model=` instead.

    Wishlist
    --------
    1. Consider using a `UUID` that's also indexed
        - We want to join on the `ID` field, not the `UUID`!
    """
    fruits = await (
        Fruits.select(
            Fruits.all_columns(exclude=[Fruits.id, Fruits.color]), # Return the fruits table
            Fruits.color.all_columns() # Join on the colors table
        ).output(nested=True) # (5)
    )

    return fruits



@fruits_router.get(
        "/{id}",
        response_model=FruitsModelOut,
        # dependencies=[Depends(transaction)]
        )
async def retrieve_fruit(id: str):
    """Retrieve a particular fruit

    #! Bug
    ------
    > Using `.first()` with an `ID` that doesn't exist returns `None`
    
    If we're coding in a data style, it's probably better to check for `[]` empty
    and access first item with indexes. It's a small difference, but it avoids us
    dealing with the `None` type (which isn't a great concept).
    """
    fruit = await Fruits.select().where(Fruits.id == id)

    #! Check for empty list (not `None`, see above)
    if fruit:
        return fruit[0]
    
    HTTPException(
        status_code=404,
        detail=f"Fruit with ID: {id} does not exist"
    )

# ------------------------------------------------------------------------------
# Write operations
# ==============================================================================
# > Protected by the `auth.authenticate` function, but no user-level checks yet.
# > If you're logged in, you can post.
#
# Be sure to handle `[]` empty and singleton (and perhaps sometimes, many). If
# you're confident your data only has one row, use `list[0]` or `.first()`


@fruits_router.post(
        "/",
        # dependencies=[Depends(transaction)]
        response_model=FruitsModelOut
        )
async def create_fruit(
    data: FruitsModelIn,
    user: str = Depends(authenticate) # Must be logged in
    ):
    """Create a new fruit

    Coding style
    ------------
    > ⚠️ ALWAYS make sure you've checked for duplicates (SQLite integrity error).
    > Use a data style (like Elm) where possible!

    `.insert()` can be provided a list of values, whereas `.update()` can only
    be provided ONE. For this reason, the internal `Fruits()` object is needed.

    We provide each `Fruit()` with a `**data` dictionary. If required, you can
    always `exclude_unset=` or `exclude_none=` here (I'm not sure you'd need to).

    
    UUID
    ----
    > The `UUID` is handled automatically by Piccolo


    Foreign keys
    ------------
    > The `ID` is the most correct way to add a foreign key entry

    You could use `String` (the name) as that's also unique, but generally it's
    safest to use an `ID` or `UUID` where possible. You can always store this on
    the frontend as a `Tuple ID String`.
    

    Returning values
    ----------------
    > `.insert()` -> `[{'id': 1}]`

    We can pull the `ID` from the response that Piccolo gives or the `:id` in
    the route provided. `.insert()` has no `.first()` method, so you've got to
    use indexes.

    
    Security
    --------
    Our Pydantic types only validate that data is a certain type. It won't protect
    us from malicious code, so consider your threat risk.


    Wishlist
    --------
    1. Convert `UUID` to use `default_factory`?
    2. Deal with errors on frontend or backend (or both?):
        - Is wrong data possible? (Pydantic doesn't cover XSS injection?)
        - `sqlite3.IntegrityError: UNIQUE constraint failed: colors.name`
    3. Check speed of creating a new fruit (or joining)
    """
    inserted = await (
        Fruits.insert(Fruits(**data.model_dump()))
        .returning(*Fruits.all_columns())
    )

    return inserted[0]



@fruits_router.put("/{id}")
async def update_fruit(
    id: str,
    data: FruitsModelIn,
    user: str = Depends(authenticate) # Must be logged in
):
    """Create a new fruit (if logged in)

    ⚠️ `RETURNING` is essential
    ---------------------------
    > Without the `returning()` option, Piccolo will return an `[]` for both
    > "row exists and has been updated" and "row does not exist", so our exception
    > would be wrong. This is a failing of SQL (no way to return affected rows?).

    Always use `.returning(*Table.all_columns())` on `UPDATE`! Without this
    function you'd need to run a `select()` first, or use `NOT EXISTS` in raw SQL,
    to discover if the row existed before updating it.

    
    Data checks
    -----------
    > Full `json` data required (except `ID` and `UUID`, handled automatically).
    > Eventually other fields (such as timestamp) may need automatically updating.

    There is no need to use `select()` first to "get" the fruit and check that it
    exists. Therefore we don't need to check if it's empty, singleton, or many.
    If we've setup our `POST` correctly, there should only be ONE entry.

    Optional data
    
    - Check for `null` fields that are optional and provide correct data.

    
    ⚠️ Positive or negative guards?
    -------------------------------
    > It may be better to use a negative guard if we've got more than one check.
    > #! We're not currently checking it's the correct user's data.

    For example, if we're validating our user, we'd need to both: `if not user`
    and `if not fruit` (each with a different `HTTPException`). I'm not sure two
    different exceptions is possible with positive guards.

    
    SQLite
    ------
    > SQLite defaults to accept whatever data you give it by default ...

    See Data integrity in `fruits.tables`. Make sure you properly validate the
    `DataIn` and `DataOut` with a Pydantic model (and any other checks you need).
    It's probably not enough to only check it on the frontend.


    Wishlist
    --------
    1. Use a `UUID` that's also indexed
        - We want to join on the `UUID` not the `ID`
        - We shouldn't need a separate `ID` field for this.
    2. Fix `sqlite3.IntegrityError: NOT NULL constraint failed: fruits.url` error
        - `UUID` (url) is automatically generated, so we shouldn't supply it.
        - We should eventually create a custom Pydantic model (rathern than using
          `create_pydantic_model`).
        - We must `exclude_unset` to avoid adding fields we don't want!
        - Does Elm frontend need to know about (or supply) the `UUID`?
            - (1) Have Elm Lang supply original `UUID`
            - (2) Have the route handle it?
    3. What data is best practice to return to the client?
        - We want a ERROR CODE if something goes wrong ...
        - As well as a error message to present to the user.
    4. How can we assure that all data is correctly updated?
        - What's optional and what's required?
        - What do we provide (or exclude) if it's optional?
        - What data do we NOT want the user to supply?
    5. What errors could happen on an `update` function?
        - Invalid data (400) or Row not found (404)
        - ⚠️ I think it's safer to always return 400 for security reasons
        - SQLite errors (not null, not supplied, ...)
        - Positively or negatively errored (`if not fruit`, `if not user`)
    """
    fruit = await (
            Fruits.update(**data.model_dump(exclude_unset=True)) #! Careful (1, 2)
            .where(Fruits.id == id)
            .returning(*Fruits.all_columns()) #! This is essential!
        )
    
    if not fruit:
        HTTPException(
            status_code=400,
            detail=f"There was a problem with your request" #! (5)
        )
    
    return { "message": f"Fruit with {id} has been successfully updated!" }



@fruits_router.delete(
        "/{id}",
        status_code=204
        # dependencies=[Depends(transaction)]
        )
async def delete_fruit(
    id: str,
    user: str = Depends(authenticate)
    ):
    """Delete a fruit

    We don't need a `return` value here as there's nothing to return. We could
    also check that item exists, but for security reasons it's probably better
    to be opaque about which `:id`s hold a database entry.


    SQlite
    ------
    > Make sure the `DELETE` cascades correctly and doesn't leave orphaned rows.

    By default I think Piccolo sets this up properly for foreign keys.


    Security
    --------
    > `DELETE` operations can torpedo your application, so be extremely careful!

    Always check the user has permission to delete the record first, and never
    add a route you don't need (especially for high risk / consequences).

    
    Status
    ------
    > FastApi expects a response body unless it's `204`!

    You could've responded with a `{"message": "Deleted {id}}` here, but might
    be a bit better for security to use a `204` with no response body. It declares
    success without a message.

    
    Wishlist
    --------
    1. Must be logged in (and the user who supplied the fruit?)
    2. Add a `.callback(check_record_not_found)` for "NOT FOUND"?
        - See `agsi new` and the `check_record_not_found()` function!
    """
    await Fruits.delete().where(Fruits.id == id)
