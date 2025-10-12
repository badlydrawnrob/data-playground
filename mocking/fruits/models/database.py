from piccolo.table import Table
from piccolo.columns import Varchar, ForeignKey

# ------------------------------------------------------------------------------
# Fruits database models
# ==============================================================================
# > Tables are given a primary key column called id, which is an auto incrementing integer.
# > There's experimental support for specifying a custom primary key column (the
# > commented out UUID field below).
#
# Notes
# -----
# 1. Class declaration order matters! (`Fruits` has `Colors` as foreign key)
#    - If `Colors` is beneath `Fruits` it errors: `'Colours' is not defined`
#
# 1. Should shorter UUIDs be handled on the client side? The route function?
# 2. Are SQLite entries validated as unique? Pydantic?
# 3. What's the average url length for an image API?
# 4. Any sensitive columns can be marked as `secret=True` (nice!)
#    - Omits that field from the `select()` query (handy for responses)
#    - `Band.select(exclude_secrets=True)`
#    - You're joining on foreign keys, so does that need exluding at all?

class Colors(Table):
    name = Varchar(length=50)
    hex = Varchar(length=7)  # e.g. #FF5733

class Fruits(Table):
    # id = UUID(primary_key=True) # (1)
    name = Varchar(length=50, unique=True) # (2)
    image = Varchar(length=255, null=True) # (3)
    color = ForeignKey(references=Colours) # (4)
