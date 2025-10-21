# ------------------------------------------------------------------------------
# Fruits database models
# ==============================================================================
# > @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/schema/index.html
#
# Piccolo `INSERT`s the values in order of the class fields; I've ordered them
# alphabetically (except the `ID` field) — it's a personal preference. See the docs
# for Column arguments, with popular ones including `null=`, `default=`, `unique=`,
# `index=`, `secret=`. Also wise to stick to naming conventions for table names
# (singular vs plural).
#
#
# Data integrity
# --------------
# > SQLite defaults to accept whatever data you give it ... it's not strict!
# > @ https://sqlite.org/stricttables.html to enforce strict tables.
#
# So ... ALWAYS validated the `DataModelIn` before inserting!
#
# If you want to enforce strictness, make it a strict table. Unfortunately this
# will mean our Piccolo columns aren't available and you'd have to stick to a
# narrower range of column types (`Integer`, `Real`, `Text`, `Blob`). Moving to
# Postgres has a better range of types.
#
# NOT ALPHABETICAL: Piccolo seems to enter data in order of the class fields:
#
# ```
# -- agsi new
# INSERT INTO "task" ("id","name","completed")
# ```
#
#
# Unique constraints
# ------------------
# > Things like `movie.id` and `move.uuid` should have a `UNIQUE` constraint
#
# This makes sure there'll be no conflicts when searching the database. It is
# important to note that a `UNIQUE` constraint does not prevent `NULL` values,
# as `NULL` is considered distinct from all other values, including other `NULL`s
# so make sure the field is `NOT NULL` as well!
#
#
# Altering the table
# ------------------
# > SQLite has limited support for `ALTER TABLE` statements.
#
# Changes can be achieved by recreating the table with the desired constraint or
# changes and copying the data. Better to use `sqlite-utils` or move to Postgres.
#
#
# UUID
# ----
# > Fruits uses the default `UUID` column, which is stored as `String` or text.
# > We have an incrementing integer (`ID` Serial) which Piccolo handles, and a
# > business identifier (`UUID`) for urls.
#
# You'll probably want to make the `ID` field `secret=` so it's harder for data
# scrapers (the whole reason to use a uuid!).` In _this_ case, you can create an INDEX on the
# > column, but it's still just text, so speed will be slower than `Int` or bytes.
#
# 1. A custom primary key column for a business identifier (`uuid`)
#     - Postgres stores `UUID`s in bytes, which is faster to search and join on
#     - We want a `shortuuid`, `nanoid`, or `fastnanoid` (untested) for URLs
#     - @ https://github.com/piccolo-orm/piccolo/issues/1271#issuecomment-3395347091
#     - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/schema/advanced.html#how-to-create-custom-column-types
#     - @ https://tinyurl.com/da2acfb-uuid-fast-api-08 (speed tested)
# 3. In the future, you can speed up your `UUID` searches and joins by:
#     - Storing as `UUID` in bytes which will be faster
#     - Convert `UUID` -> short UUID in the route function (with base64 encoding)
#     - Or, use Elm on the client to encode/decode (speed test both options)
#
#
# One-to-one relationships
# ------------------------
# > There's a couple of ways to enter a foreign key relationship
#
# 1. Use the `ID` of the related table (e.g: Elm `(Int, Color)` tuple)
# 2. Use the related object itself (e.g: `Color` object)
#
#
# #! Performance
# --------------
# > It's too early to worry about performance, but you'll probably move to Postgres
# > in the future and then ...
# 
# Use better types such as `Int` or bytes for a faster search/join as mentioned
# above in the `UUID` section.
# 
#
# Notes
# -----
#
# 1. Are SQLite entries validated as unique? Pydantic?
# 2. Sensitive columns can be marked as `secret=True` (nice!)
#    - Omits that field from the `select()` query (handy for responses)
#    - `Band.select(exclude_secrets=True)`
#    - You're joining on foreign keys, so does that need exluding at all?
# 3. For now we're simply using emojis ...
# 4. Short `UUID`s can be handled in DB, route function, or the client:
#    - @ https://dba.stackexchange.com/questions/307520/how-to-handle-short-uuids-with-postgres
# 5. Piccolo stores `null` values as `None` in the SQLite database
#
#
# Wishlist
# --------
# 1. What's the average url length for an image API?
# 2. Does class field order matter or just use alphabetical order?

from piccolo.table import Table
from piccolo.columns import ForeignKey, Varchar, UUID


class Colors(Table):
    """
    This table must be declared before `Fruits`, or
    you'll get `'Colours' is not defined` error!
    """

    color = Varchar(length=7)      # e.g. #FF5733
    background = Varchar(length=7) # e.g. #C70039
    name = Varchar(length=50, unique=True)


class Fruits(Table):
    """
    `id` is by default an auto-incrementing
    integer primary key. `UUID(primary_key=True)`.
    """

    color = ForeignKey(references=Colors)  # (2)
    image = Varchar(length=255, null=True) # (3)
    name = Varchar(length=2, unique=True)  # (4)
    url = UUID()
