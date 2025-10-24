# ------------------------------------------------------------------------------
# Fruits database models
# ==============================================================================
# > @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/schema/index.html
# > @ https://github.com/piccolo-orm/piccolo/issues/1257
#
# Piccolo with SQLite names it's Column types, but in reality they're stored as
# basic SQLite data types: `Integer`, `Real`, `Text`. `Blob` is also there but I
# don't think Piccolo uses it (Postgres has a wider range of types).
# 
# `INSERT`s the values in order of the class fields; I've ordered them
# alphabetically (except the `ID` field) — it's a personal preference. See the docs
# for Column arguments, with popular ones including `null=`, `default=`, `unique=`,
# `index=`, `secret=`. Also wise to stick to naming conventions for table names
# (singular vs plural).
#
# ```sql
#  -- agsi new
# INSERT INTO "task" ("id","name","completed")
# ```
#
# Insertion is handled in the order you declare your table class fields, NOT in
# alphabetical order, so pick a convention and stick with it!
#
#
# Data integrity
# --------------
# > SQLite defaults to accept whatever data you give it ... it's not strict!
# > @ https://sqlite.org/stricttables.html to enforce strict tables.
#
# So ... ALWAYS validated the `DataModelIn` before inserting!
#
# Making SQLite use strict tables is safer, but limits the range of Column types
# Piccolo uses (even if they're still using SQLites basic underlying types. If
# you're validating data with Pydantic first, there shouldn't be any problems.
# Postgres has better support for the wide range of types Piccolo uses, such as
# `jsonb` and `UUID`. Hopefully migrating data to Postgres will make use of this.
#
#
# Required values
# ---------------
# > By default it seems ALL values are optional and can be `None`.
# 
# So if it's required, you must validate it before inserting (I don't think
# SQLite will catch it!
#
# - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/serialization/index.html#required-fields
#
#
# Unique constraints
# ------------------
# > Things like `movie.id` and `move.uuid` should have a `UNIQUE` constraint.
# > SQLite validates that a value is unique if it's set. `Null values` are not
# > considered equal (distinct), so make sure `NOT NULL` is set!
#
# ```
# #! sqlite3.IntegrityError: UNIQUE constraint failed: colors.name
# ```
#
# If there's a unique constraint conflict, you'll have to notify the user:
#
# 1. Use a `try/except` block to catch the `sqlite3.IntegrityError`
# 2. Handle this in Elm by `caseing` on the `Colors` list
#
#
# Indexing
# --------
# Indexing columns speeds up the search and joins.
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
# > Fruits uses the default `UUID` column for it's business identifier, and you'll
# > want the `ID` (Serial) to be hidden in the API response (see Secrets)
# 
# `UUID` gets stored as `Text` in the database (a Pydantic `String`). Piccolo 
# automatically handles the regular `ID` fields which are incremented. We can use
# the business identifier for public URLs instead of the `ID` field.
#
# You'll also want to use short UUIDs for prettier URLs:
#
# - @ https://github.com/piccolo-orm/piccolo/issues/1271#issuecomment-3395347091
#
# You might want to create your own custom Column type:
#
# - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/schema/advanced.html#how-to-create-custom-column-types
# 
# 
# Performance
# -----------
# > A `String` is never going to be as fast as an `Int`, but it's probably fast
# > enough for a prototype. Postgres may have better performance (using `bytes`).
# >
# > @ https://tinyurl.com/da2acfb-uuid-fast-api-08 (speed testing short UUIDs)
#
# In the future you'll want to use `shortuuid`, `nanoid`, or `fastnanoid` (untested)
# to handle your URL ids. There's a few ways to handle this:
#
# 1. Store the short UUID in the backend using `Text` column
# 2. Store the full `UUID` in bytes (with Postgres) on the backend, then:
#     - Convert to a short UUID in the route function
#     - Convert to a short UUID in the client code (javascript)
#
# #! I'm not sure how performance will be affected by converting from a `UUID` to
# a `fastnanoid`, for example. But it seems faster than generating a `fastnanoid`
# directly. You could always use an Elm decoder and test that. Research needed.
#
# #! It's too early to worry about general peformance, but it's likely I'll move
# to Postgres when I have a team member.
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
# Secret columns
# --------------
# > API responses should have certain fields made `secret=`, such as the `ID` field,
# > which helps prevent against brute force attacks and data scraping.
# 
# Use with `Band.select(exclude_secrets=True)` arguments. For the `id` field there
# are two options:
# 
# 1. `id = Serial(secret=True)`
# 2. `exclude_columns=Table.id` with `create_pydantic_model`
#
#
# Notes
# -----
# 1. You're joining on foreign keys, so does that need exluding at all?
# 2. For now we're simply using emojis ...
# 3. Short `UUID`s can be handled in DB, route function, or the client:
#    - @ https://dba.stackexchange.com/questions/307520/how-to-handle-short-uuids-with-postgres
# 4. Piccolo stores `null` values as `None` in the SQLite database
# 5. There's two ways to generate this:
#    - `create_pydantic_model` then manually use the `uuid.uuid4()` function
#    - Custom Pydantic model: `str = Field(default_factory=nanoid.generate)`
#
#
# Wishlist
# --------
# 1. What's the average url length for an image API?
# 2. Does class field order matter or just use alphabetical order?
# 3. Test the following for speed:
#     - Indexed `UUID` join
#     - Get `ID` with `UUID` ==, then join on `ID`

from piccolo.table import Table
from piccolo.columns import ForeignKey, Varchar, Serial, UUID


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
    
    id = Serial(secret=True)               # (1)
    color = ForeignKey(references=Colors)  # (2)
    image = Varchar(length=255, null=True) # (3)
    name = Varchar(length=2, unique=True)  # (4)
    url = UUID()                           # (5)
