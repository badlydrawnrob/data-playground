from piccolo.table import Table
from piccolo.columns import Varchar, ForeignKey

# ------------------------------------------------------------------------------
# Fruits database models
# ==============================================================================
# > @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/schema/index.html
#
# I need to understand how `default=` works. Also decide whether to use the
# singular or plural form for table names (`Fruit` vs `Fruits`).
#
# UUID
# ----
# There's experimental support for specifying a custom primary key column, but we
# want the primary keys (id: Serial) versus business identifiers (uuid: UUID)
# pattern: @ https://github.com/piccolo-orm/piccolo/issues/1271#issuecomment-3395347091
#
# Notes
# -----
#
# 1. Are SQLite entries validated as unique? Pydantic?
# 2. Short `UUID`s can be handled in DB, route function, or the client:
#    - @ https://dba.stackexchange.com/questions/307520/how-to-handle-short-uuids-with-postgres
# 3. What's the average url length for an image API?
# 4. Sensitive columns can be marked as `secret=True` (nice!)
#    - Omits that field from the `select()` query (handy for responses)
#    - `Band.select(exclude_secrets=True)`
#    - You're joining on foreign keys, so does that need exluding at all?

class Colors(Table):
    """
    This table must be declared before `Fruits`, or
    you'll get `'Colours' is not defined` error!
    """

    name = Varchar(length=50)
    hex = Varchar(length=7) # e.g. #FF5733


class Fruits(Table):
    """
    `id` is by default an auto-incrementing
    integer primary key. `UUID(primary_key=True)`.
    """

    name = Varchar(length=50, unique=True) # (2)
    image = Varchar(length=255, null=True) # (3)
    color = ForeignKey(references=Colors)  # (4)
