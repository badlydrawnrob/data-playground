# ------------------------------------------------------------------------------
# Routes
# ==============================================================================
# > We're using `@fruits_router` rather than `@app` here as it's better organised.
# > You need to register the router in `app.py` with `include_router`.
#
# See `fruits.models` for information on our model types.
#
#
# Requests
# --------
# > You can use `status=` in the decorator instead of response if needed
# > @ https://docs.pydantic.dev/latest/concepts/serialization/
#
# - You can use named arguments with types for clarity
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
# Most functions (like `.delete()`) return no values (an empty `[]`). You can use
# `.returning()` if you need to add values to the response. Take care with security
# you don't expose anything important!
#
#
# Connection to the database
# --------------------------
# > This is handled automatically, no need to `open()` and `close()`
#
# Piccolo handles connections, but you may need to add transactions when you're
# dealing with concurrent requests (see `app.py` notes).
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
# 1. ⭐ Somewhere check for UNIQUE values (either `try/except` or Elm)
#    - `#! sqlite3.IntegrityError: UNIQUE constraint failed: colors.name`
# 2. Handle all errors "just in time" (you'll not catch them all upfront)
#    - See `chapter_03` of "Building with FastApi" for full checks (like `[]` empty)
#    - Make sure to use logs and have people send enough data to replicate bug
#    - Make sure to thoroughly test your API with Bruno for correct and incorrect data
# 3. Make some routes IMPOSSIBLE (things that are destructive and Admin only)
#    - `DELETE` all `fruits/` will torpedo your database!
#    - Better to use a tool like `sqlite-utils`, a GUI, or no-code dashboard
# 4. Currently getting `.first()` with `[0]` as there should only be ONE
#    - You've got to be super strict with your UNIQUE values for this however
# 5. You _could_ use Piccolo `create_pydantic_model` with `nested=True`, but in
#    general it's better to generate your own custom Pydantic type for joins.
#    - The more complex the join, the harder it is for Piccolo "magic"!
#
#
# Wishlist
# --------
# 1. Include the original auth function from "building with FastAPI"
#     - HS256 is perfectly fine if you own the stack (see `README.md`)
#     - Enforce logged in and verified user (just one account)
#     - Change "claims" to not hold any sensitive data (only a `UUID`)
#     - A single function that returns an `HTTPException` if not logged in
# 2. Understand and implement the `BaseUser` table properly
#    - And how does it differ from `piccolo_user` table?
#    - @ https://github.com/sinisaos/simple-piccolo/blob/main/fastapi_app.py#L73
#    - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/authentication/baseuser.html#baseuser
#    - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/authentication/baseuser.html#extending-baseuser
# 3. Write an endpoint to get basic user preferences
# 4. How to make sure of XSS protection (ask Mike)
# 5. Create a filter, pagination, and search route?
#     - Investigate `case` in Python` to validate query strings
#     - @ https://stackoverflow.com/a/11479840 (Python 3.10+)
# 6. Transactions: understand when to be careful with `select()` then writes
# 7. Performance: which is faster? Object oriented or data? Safer?

from fastapi import APIRouter, HTTPException

from fruits.models import FruitsModelIn, FruitsAllModelOut, FruitsModelOut
from fruits.tables import Fruits, Colors

from typing import List
from uuid import uuid4


fruits_router = APIRouter(
    tags=["Fruits"] # used for `/redoc` (menu groupings)
)


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
    1. Join on the `Fruit.id` field and not the `UUID` field
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
async def retrieve_fruit(id: int):
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
# Be sure to handle `[]` empty and singleton (and perhaps sometimes, many). If
# you're confident your data only has one row, use `list[0]` or `.first()`


@fruits_router.post(
        "/",
        # dependencies=[Depends(transaction)]
        response_model=FruitsModelOut
        )
async def create_fruit(
    body: FruitsModelIn,
    # user: str = Depends(authenticate)
    ):
    """Create a new fruit

    Coding style
    ------------
    > Use a data style (similar to Elm Lang) wherever possible

    `.insert()` can be provided a list of values, whereas `.update()` can only
    be provided ONE. For this reason, the internal `Fruits()` object is needed.

    We provide each `Fruit()` with a `**data` dictionary. If required, you can
    always `exclude_unset=` or `exclude_none=` here (I'm not sure you'd need to).

    
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
    uuid = uuid4()
    body.url = uuid

    inserted = await (
        Fruits.insert(Fruits(**body.model_dump()))
        .returning(*Fruits.all_columns())
    )

    return inserted[0]


    


@fruits_router.put("/{id}",
        # dependencies=[Depends(transaction)]
        )
async def update_fruit(
    id: int,
    data: FruitsModelIn,
):
    """Create a new fruit (if logged in)

    Data checks
    -----------
    > You must provide the full data required to update the entry. Fields like
    > `ID` and `UUID` should not be changed. Eventually, some fields (such as
    > timestamp) may need automatically updated.

    Lists can be:
    
    - Empty? `if list`
    - Singleton? `if len(list) == 1`, or `(single,)` which returns `ValueError`
    - Many? (shouldn't be required)

    Fields can be:

    - null? Be sure that fields that are optional provide correct data

    
    Positive or negative guards?
    ----------------------------
    > It may be better to use a negative guard if we've got more than one check.

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
    1. Fix `sqlite3.IntegrityError: NOT NULL constraint failed: fruits.url` error
        - We shouldn't supply the `url` as it's an automatic `UUID` ...
        - Currently we're using `exclude_unset` and a default `create_pydantic_model`
        - (1) Have Elm Lang supply original `UUID` | (2) Have the route handle it?
    2. Change `ID` to `UUID` and search on that?
    3. Run a speedtest on the backend and frontend
    4. What data is best practice to return to the client?
    5. How can we assure that all data is correctly updated?
        - What's optional and what's required?
        - What do we provide (or exclude) if it's optional?
        - What data do we NOT want the user to supply?
    6. What errors could happen on an `update` function?
        - SQLite errors (not null, not supplied, ...)
        - Positively or negatively errored (`if not fruit`, `if not user`)
    """
    fruit = await Fruits.select().where(Fruits.id == id) # A list (singleton)

    if fruit: #!
        await (
            Fruits.update(**data.model_dump(exclude_unset=True)) #! Careful (1)
            .where(Fruits.id == id)
        )

        #! Must be a proper json type or dictionary!
        #! WEIRDNESS GOES HERE!!!
        return { "message": f"Fruit with {id} has been successfully updated!" }

    HTTPException(
        status=400, #! Is this the correct status code?
        detail=f"There was a problem with your request"
    )




@fruits_router.delete(
        "/{id}",
        status_code=204
        # dependencies=[Depends(transaction)]
        )
async def delete_fruit(
    id: int,
    # user: str = Depends(authenticate)
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
