from fastapi import APIRouter, Depends, HTTPException

from api import FruitsIn, FruitsOut
from database import Colours, Fruits

from typing import List

# ------------------------------------------------------------------------------
# FRUITS routes
# ==============================================================================
# > Here we setup our app routes. We've split out our API and DATA models, and are
# using Piccolo ORM.
#
# Response types
# --------------
# > Should you use `response_model=` or a response type?
# > I don't think you should be using both at the same time?
#
# For sensitive information in the response, such as `User.id`, we can either use
# `response_model=` (with a Pydantic API model) or `Varchar(secret=True)`
# (with our DATA model). The latter omits that field from the `select()` query.
#
#
# Questions
# ---------
# 1. How do we test concurrent connections for read and write?
#    - How many connections can SQLite handle?
# 2. Does Piccolo ORM have a `None` type?
#    - (`.select()` can return `[]` an empty list)
# 3. What's the difference between a response type and `response_model=`?
#    - Why is `response_model=` used in some cases and not others?
# 4. What are named keyword arguments and how do they work?
#    - `session=Depends(get_session)` (sometimes it has a type also)
# 5. Why `data.model_dump(exclude_unset=True)`?
#    - Removes any `None` values that haven't been set.
# 6. When to use `PATCH` vs `PUT` requests? (see tag `1.10.4`)
#    - `PATCH` could have any number of `Optional` fields not set
#    - `PATCH` has no way of knowing which data is present so Piccolo would need
#      to be flexible with it's update function. Use objects?
#    - @ https://fastapi.tiangolo.com/tutorial/body-updates/#update-replacing-with-put
# 7. `Depends()` can go in the route decorator AND route function.
#    - What's up with that?!
#
#
# User experience
# ---------------
# > See the "Van Man Problem" for API architecture and design.
#
# 1. `Delete` operations should always prompt the user to confirm.
# 2. Handle errors correctly. Don't leak sensitive information.
# 3. Authenticate all routes that require authentication, or are "risky".
#    - Make sure it's the correct user that is allowed to edit their posts.
# 4. What data should be public? What data should be private?
#
#
# Bugs
# ----
# 1. ⭐ Be aware of duplicates when a field is supposed to be unique!
#    - I don't think Piccolo's SQLite engine enforces this by default?
# 2. Make sure all errors are handled
#    - See `chapter_03` of "Building with FastApi" for full checks (like `[]` empty)
#    - Make sure to thoroughly test your API with Bruno for correct and incorrect data
# 3. Some routes should NEVER be possible (admin only)
#    - `DELETE` all `fruits/` will torpedo your database!
#    - Better to use a tool like `sqlite-utils`, a GUI, or no-code dashboard
# 4. Know the difference between a `Band.select()` and `Band.objects()`
#    - The former will return a list of dictionaries!
#    - Use objects VERY sparingly, but could be useful for `PATCH` updates
#
#
# Wishlist
# --------
# 1. Create a `@fruit_router.patch("/edit/{id}"` route?
# 2. Create a filter, pagination, and search route?
# 3. Write the authentication function (see Piccolo issues)

fruit_router = APIRouter(
    tags=["Fruits"] # `/redoc` endpoint (menu groupings)
)


# Routes -----------------------------------------------------------------------
# 1. #! Why the fuck are we using `response_model` AND a response type?!
# 2. `Depends()` (always?) runs first before the route function executes.

@fruit_router.get("/", response_model=List[Fruits], dependencies=[Depends(transaction)]) #!
async def retrieve_all_events() -> List[Fruits]:          #!
    """Return all fruits

    > #! I don't think you need BOTH `response_model=` and a response type?

    Aim to write your functions in Elm style as much as possible, which isn't
    mutable. Don't force Python to do what it's not meant to do, however. Maybe
    objects are OK when used in moderation.

    1. Create a pydantic model for API
    2. Create a pydantic model for DATA
    3. Get all fruits
    4. Join on Colors table
    5. Return the fruits
    """
    pass


@fruit_router.get("/{id}", response_model=Fruit, dependencies=[Depends(transaction)])
def retrieve_event(id: int) -> Fruit:
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


@fruit_router.post("/new", dependencies=[Depends(transaction)])
def create_event(
    body: Fruit,
    user: str = Depends(authenticate)) -> EventWithCreator:
    """Create a new fruit (if logged in)

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
    """
    pass



@fruit_router.delete("/{id}", dependencies=[Depends(transaction)])
def delete_event(id: int, user: str = Depends(authenticate)) -> dict:
    """Delete a fruit (if logged in)

    See the events route for more info on `if` statements and error handling.
    Make sure the `DELETE` cascades correctly and doesn't leave orphaned rows.
    """
    pass
