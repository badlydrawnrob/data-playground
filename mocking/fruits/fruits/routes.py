# ------------------------------------------------------------------------------
# Routes
# ==============================================================================
# > We're using `@fruits_router` rather than `@app` here as it's better organised.
# > You need to register the router in `app.py` with `include_router`.
#
# See `fruits.models` for information on our model types.
#
#
# Coding style is a personal preference
# -------------------------------------
# > Technically not 100% data style as we're using Pydantic types and assigning
# > some arguments in the route function. DRY is great but overused: similar is
# > not the same as identical.
#
# See also `app.py` "Learning frame" for coding standards.
#
# In general, I prefer working with data rather than objects (no classes, no
# methods, no weird decorators). I'll leave in both examples and then it's up to
# the individual to decide which they prefer.
#
# However, some functions may benefit from an oject oriented style as they're less
# code and (potentially) quicker than a typed functional style, such as updating
# a single field. With `update_task` we have to do some gymnastics with a data style.
#
# Aim for minimalism wherever possible: `Task._meta.primary_key` -> `Task.id`.
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
# > You can use `status=` in the decorator instead of response if needed
# > @ https://docs.pydantic.dev/latest/concepts/serialization/
#
# - You can use named arguments with types for clarity (#! `body` -> `data`)
# - You can use `(**kwargs)` to `data.model_dump()` a dictionary into a model
# - You can use `.model_dump(exclude_unset=True)` to remove `None` fields
# - You can use `PUT` or `PATCH` to update data, but `PUT` is far more explicit
#
#
# PATCH -vs- PUT
# --------------
# > In general I feel it's better to be explicit unless there's a good reason
# > not to. So, store all fields in Elm model, then `PUT` with updated values.
#
# 1. Use dedicated routes (not patch) for `user` and `user.settings`
#     - Google does this for forms like "password" (a form/route for each data)
# 2. It's probably better to be explicit and reset ALL data
#     - This prevents any conflicts or accidentally changing a field
#
# The problem with `PATCH` is it can have any number of `Optional` fields not set,
# and there's no way of knowing which data is present in the request body.
#
# That's not a huge problem in and of itself, but you'll have to be careful to
# make sure the DB doesn't get wrong values. Also remember @lydell's note about
# `Json.Decode` and using `nullable` rather than `maybe` with missing values.
#
# `PUT` is idempotent, meaning multiple identical PUT requests always has the
# same result.
#
#
# Responses
# ---------
# > Take care to use the proper status codes for each operation! See also the
# > Serialization section in `fruits.models`.
#
# Types:
# Use either `response_model=` or `->` response type (unlikely you'll need both)
#
# Security:
# By default Piccolo hides the `ID` field from the response. Hide sensitive information
# with `response_model=` or Piccolo `secret=True`, and use `Depends()` to check
# JWT tokens (if declared this always runs first, before route function body)
#
# Singleton:
# For `.select()` and `.objects()` you can always use `.first()` if you're confident
# there's only supposed to be a singleton response.
#
# Returning:
# > SQLite 3.35.0 and above supports the returning clause.
# > Use `first()` on functions that allow it (and `list[0]` otherwise)
#
# Returning values are essential for some endpoints to work correctly! See
# `update_fruit` for an example. Most functions (like `.delete()`) return no values
# (an empty `[]`). You can use `.returning()` if you need to add values to the
# response. Take care with security you don't expose anything important!
#
#
# Connection to the database
# --------------------------
# > SQLiteEngine has no `connect()` and `close()` functions to open/close the
# > `fruits.sqlite` database.
#
# Piccolo handles connections automatically, but you may need to add transactions
# when you're dealing with concurrent requests (see `app.py` notes).
# 
#
# 
# Saving entries into the database
# --------------------------------
# > See "serialization" in `fruits.models.py` to understand `.model_dump()` ...
# > and know the difference between a `Band.select()` and `Band.objects()`!
#
# Pick a convention: data style (or Object Oriented style). Sometimes the OOP
# style can result in a little less code.
#
# 1. When we're working with queries, we can use `.add()` or `.insert()`
# 2. When we're working with objects, we can use `.save()`
#
#
# Database exceptions
# -------------------
# > @ https://docs.python.org/3/tutorial/errors.html#exceptions
#
# - Not defined
# - No DB results for query
# - Null not allowed
# - No duplicate entry values
#
#
# Questions
# ---------
# 1. How do we test concurrent connections for read and write?
#    - How many connections can SQLite handle?
# 2. When do queries not return an `[]` empty list?
#    - `Band.objects().get(Band.id == 1)` will return single object (no list)
# 3. What's the difference between a response type and `response_model=`?
#    - Why is `response_model=` used in some cases and not others?
# 4. What are named keyword arguments and how do they work?
#    - `session=Depends(get_session)` (sometimes it has a type also)
# 5. `Depends()` can go in the route decorator AND route function.
#    - What's up with that?!
#
#
# Bugs
# ----
# 1. ⚠️ Be stricter with UNIQUE values for insert (which effects response)
#     - Currently "Internal Server Error" for unique constraint fails
#     - Create a code for this particular error (see APIs you won't hate)
#     - If you've ensured all entries are unique throughout the stack, then
#       `fruits[0]` and `.first()` should be totally fine to use.
# 2. ⚠️ IMPOSSIBLE routes: anything that's destructive or hackable ...
#    - Do admin stuff offline with `sqlite-utils`, GUI, or no-code. Wait until
#      you can hire a professional to build out a secure platform (with roles)
#    - `piccolo-admin` and `piccolo user create` are good examples of this
#    - `DELETE` all `fruits/` is a terrible idea and will kill your database
#
#
# Wishlist
# --------
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
#    - @ 

from auth.authenticate import authenticate
from auth.jwt_handler import create_access_token

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from fruits.models import FruitsModelIn, FruitsAllModelOut, FruitsModelOut, TokenResponse
from fruits.tables import Fruits, Colors

from piccolo.apps.user.tables import BaseUser

from typing import List
from uuid import uuid4


fruits_router = APIRouter(
    tags=["Fruits"] # used for `/redoc` (menu groupings)
)

user_router = APIRouter(
    tags=["User"]
)

# ------------------------------------------------------------------------------
# User operations
# ==============================================================================
# > Currently does not require a `client_id` value, but Bruno complains if it
# > doesn't contain some value (using `none` for now).
#
# ```
# curl -X 'POST' \
# 'http://localhost:8000/login' \
# -H 'accept: application/json' \
# -H 'Content-Type: application/x-www-form-urlencoded' \
# -d 'grant_type=password&username=[USER]&password=[PASSWORD]&scope=&client_id=none&client_secret=none'
# ```

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


    result = await BaseUser.select().where(BaseUser.id == user).first()
    token = create_access_token(result["username"])

    return {
        "access_token": token,
        "token_type": "Bearer"
    }


# ------------------------------------------------------------------------------
# Read operations
# ==============================================================================
# > #! If you're using `response_model=` I think the response type is redundant!

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
