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
# > #! I'm a little confused with FastAPI as whether to use `response_model=` or
# > a response type hint. I don't know which is best in what context. When would
# > you ever use both?!
#
# - You can use the `response_model=` to pass a Pydantic type as the json response
# - You can also use a Pydantic type as the response type `def func() -> Type:`
# - Hide sensitive information with `response_model=` or Piccolo `secret=True`
# - `Depends()` (always?) runs first before the route function executes.
# - Take care to use the proper status codes for each operation.
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
# Coding style is a personal preference
# -------------------------------------
# > DRY is great but overused: similar is not the same as identical.
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
#
#
# Wishlist
# --------
# 1. Decide which style to use `PATCH` or `PUT` and stick to it?
# 2. Create a filter, pagination, and search route?
# 3. Performance: which is faster? Object oriented or data? Safer?
# 4. Re-write the authentication function (see Piccolo issues)
#    - Ask Mike if it's good to go! (How secure is it?)
# 5. Transactions: understand when to be careful with `select()` then writes
#     - This is only a consideration for SQLite

from fastapi import APIRouter, HTTPException

# from fruits.models import FruitsModelIn, FruitsAllModelOut, FruitsModelOut
from fruits.models import FruitsModelIn, FruitsModelOut
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
        # response_model=List[FruitsAllModelOut],
        # dependencies=[Depends(transaction)]
        )
async def retrieve_all_fruits():
    """Return all fruits

    > #! Is there a time you'd need BOTH response type and response model?

    I've removed the response type from the function, we're using the
    `response_model=` instead.
    """
    fruits = await (
        Fruits.select(
            Fruits.all_columns(exclude=[Fruits.id, Fruits.color]), # Return the fruits table
            Fruits.color.all_columns() # Join on the colors table
        )
        # ).output(nested=True)
    )

    return fruits


@fruits_router.get(
        "/{id}",
        response_model=FruitsModelOut,
        # dependencies=[Depends(transaction)]
        )
def retrieve_fruit(id: int):
    """Retrieve a particular fruit

    > #! Wherever possible there should be ONE `connect()` and `close()` function

    Aim to make data immutable where possible.
    I don't like `try/except/finally` blocks.
    I don't like the concept of `None`.
    Make sure there's no "exception" errors ...

    @ https://docs.python.org/3/tutorial/errors.html#exceptions
    (not defined, no DB results for query).

    1. See `get("/")` and follow steps
    2. If fruit doesn't exist raise 404 error
    3. `if fruit` return the fruit json
    4. Else raise 404 error with `raise HTTPException()`
    """
    pass


# ------------------------------------------------------------------------------
# Write operations
# ==============================================================================
# 1. Be sure to handle `[]` empty and singleton (and perhaps sometimes, many)
#     - If you're using object oriented style you can use `.first()`
# 2. Confident your data only has one row? Remove the singleton checks!
#     


@fruits_router.post(
        "/",
        # dependencies=[Depends(transaction)]
        response_model=FruitsModelOut
        )
async def create_fruit(
    body: FruitsModelIn,
    # user: str = Depends(authenticate)
    ) -> FruitsModelOut:
    """Create a new fruit

    We're not 100% using a data style here: it's easier using objects to assign
    a `UUID` value. We can `model_dump()` to turn into a dictionary after.

    - Piccolo handles the `ID` field automatically
    - We can set `exclude_unset=` or `exclude_none=` if needed

    Returning values
    ----------------
    > SQLite 3.35.0 and above supports the returning clause.

    By default, an update query returns an empty list, but using the `returning`
    clause you can retrieve values from the updated rows.

    Wishlist
    --------
    1. Deal with `UNIQUE` constraint failed error (from SQLite)
        - `sqlite3.IntegrityError: UNIQUE constraint failed: colors.name`
    2. Check speed of creating a new fruit (or joining)
    3. What's the best way to enter the `Color` foreign key?
    4. Enforce logged in and verified user
        - JWT should return claim (with user `sub` details)
    """
    uuid = uuid4()
    body.url = uuid

    inserted = await (
        Fruits.insert(Fruits(**body.model_dump()))
        .returning(*Fruits.all_columns())
    )

    #! `ID` should not be returned!
    #! Is there a better way to extract the single object?
    return inserted[0]


    


@fruits_router.put("/{id}",
        # dependencies=[Depends(transaction)]
        response_model=FruitsModelOut
        )
def update_fruit():
    """Create a new fruit (if logged in)

    Data checks
    -----------
    `singleton, = list` or `if len(list) == 1:` to ensure singleton results.
    The former will return `ValueError` if not a singleton.

    > SQLite defaults to accept whatever data you give it by default ...
    > it doesn't respect types unless it's a strict table. Strict tables are
    > a bit inconvenient so ALWAYS validated the `DataModelIn` before inserting.
    > Postgres is strict by default.
    >
    > @ https://sqlite.org/stricttables.html

    1. Fails if user not logged in (requires valid JWT)
    2. JWT should return a claim (with user details)
    3. Claim has `sub` value with `UUID` ...
    4. But we `JOIN` on the `User.id` field (an `int`)
    5. Be careful in the response not to expose secret data
    6. Run a speedtest on the backend and frontend
    7. What data is best practice to return to the client?

    Some fields (like the auto incrementing `id`) are created by the ORM, so
    they're not required in the POST body. We can use `exclude_none=True` to
    ignore any fields that aren't set in the request body.

    ```
    EventData(creator=username, **body.model_dump(exclude_none=True))
    # or
    { ... dict ... }
    Function(**kwargs)
    ```

    @ https://docs.pydantic.dev/latest/concepts/serialization/ (dumps)

    I imagine OCaml and Elm would do things manually, rather than using magic
    like `response_model=` and `model_dump()`?

    Returning values
    ----------------
    > Only SQLite 3.35.0 and above support the returning clause.

    By default, an update query returns an empty list, but using the `returning`
    clause you can retrieve values from the updated rows. We return the full `Task`
    object after updatating the row.
    """
    pass




@fruits_router.delete(
        "/{id}",
        # dependencies=[Depends(transaction)]
        )
def delete_fruit(
    id: int,
    # user: str = Depends(authenticate)
    ) -> dict:
    """Delete a fruit (if logged in)

    > #! What's best practice as a return body for a `DELETE` request?

    I'm using a data style and I think it's safe to just run the function even
    if the record doesn't exist. See the events route for more info on `if`
    statements and error handling. Make sure the `DELETE` cascades correctly and
    doesn't leave orphaned rows.

    Security
    --------
    > `DELETE` operations can torpedo your application, so be extremely careful.

    Check the user has permission to delete the record first.
    """
    pass
