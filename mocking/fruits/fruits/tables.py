# ------------------------------------------------------------------------------
# Fruits database models
# ==============================================================================
# > See `badlydrawnrob/python-playground/building-with-fast-api` for more docs.
# > SQLite is not as strict or flexible as Postgres; migrate to that in future?
# 
#     @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/schema/index.html
#     @ https://github.com/piccolo-orm/piccolo/issues/1257
#     @ https://github.com/piccolo-orm/piccolo/issues/1319 (Async problems)
#
# Do not worry prematurely about performance; consider it when you have users!
#
# 1. Piccolo columns are stored as basic data types in SQLite
#     - `Integer`, `Real`, `Text`, etc (Postgres has better typing)
# 2. SQLite is NOT set to strict mode, so potentially ANY value is accepted
#     - We're heavily relying on API layer models (add DATA models if you wish)
#     - Without care, potentially ANY data can be inserted without strictness
# 3. Table fields required by default `null=False` (null /= null ... NOT distinct)
# 4. Values are inserted by field order (not alphabetically)
# 5. Insertions are by field order (not alphabetical)
# 6. `sqlite3.IntegrityError` null and distinct values are a problem
#     - Duplicate checking is best handled with the DB (not the client)
# 7. Piccolo uses full joins on queries (e.g: `Fruits.color.name` is valid)
#     - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/query_types/joins.html#joins
# 8. ⏱ UUIDs (primary key) should also be INDEXED for quicker lookups.
#     - `Int > Bytes > String` performance speed (Postgres bytes is better)
#     - `order_by` defaults to INDEX row id (not UUID)
#     - ⏱ `Serial` as primary key with public UUID is another pattern
#     - Pretty URLs can be created by shortening UUID on backend/frontend
# 9. Hide fields in your Pydantic model (which ideally are custom)
#     - Primary keys are hidden by default in the response
#     - Alternatively you can use `create_pydantic_model` with `secret=True`
#
#
# One-to-one relationships
# ------------------------
# > Where you need an `ID` on the frontend, make data structures.
# > For example, a foreign key relationship can be represented like ...
#
# 1. `(Int, Colour)` tuple (foreign key `Serial` ID: potentially fastest)
# 2. `Color` dictionary/object (`Color.id` / `String` and let SQLite handle join)
#
#
# WISHLIST
# --------
# 1. Average url length for image API?
#     - @ ...
# 2. Is it better to use ABC order for class fields?
#     - Or by importance? (does order matter)
# 3. Performance speed testing (someday):
#     - Indexed `UUID` join
#     - Non-indexed `UUID` with `Serial` ID (still requires lookup by UUID?)
#     - @ https://dba.stackexchange.com/questions/307520/how-to-handle-short-uuids-with-postgres

from piccolo.table import Table
from piccolo.columns import ForeignKey, Varchar, UUID


class Colors(Table):
    """
    This table must be declared before `Fruits`, or
    you'll get `'Colours' is not defined` error!

    `id` is an auto-incrementing integer
    """

    color = Varchar(length=7)      # e.g. #FF5733
    background = Varchar(length=7) # e.g. #C70039
    name = Varchar(length=50, unique=True)


class Fruits(Table):
    """
    > We're using both `Serial()` and `UUID()` columns.

    > Primary key is `secret=True` by default (hidden in the response).

    By default Piccolo uses an auto-incrementing `id` primary key with the
    `Serial()` column type (created automatically). We've changed it here to
    use the `UUID` column type. It must be marked as the `primary_key`, so Piccolo
    knows to create it (no need for a `default_factory` in the `Table` subclass).
    
    The Elm-Land version uses emojis, but we'll test out an image server.
    """

    id = UUID(primary_key=True, index=True) # (2), (3)
    color = ForeignKey(references=Colors)
    image = Varchar(length=255, null=True)  # (1)
    name = Varchar(length=15, unique=True)
