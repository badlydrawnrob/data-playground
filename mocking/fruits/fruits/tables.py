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
# Do not prematurely optimize and worry about performance with customers.
#
# 1. Take care with inserts: SQLite is not in strict model
#     - `sqlite3.IntegrityError` is raised for null and distinct values
#     - Duplicate values are best handled with the DB (not the client)
# 2. Table fields are required by default (use `null=True` for optional)
# 3. Insertions are by field order (not alphabetical)
# 4. Primary keys are hidden in the response (use `secret=False` to show)
# 5. Foreign keys are always joined, so you can traverse them
# 6. Foreign keys that are strings should always be indexed for performance
# 7. It's more secure to not expose primary keys (but the client may need them)
#
#
# ------------------------------------------------------------------------------
# WISHLIST
# ------------------------------------------------------------------------------
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
