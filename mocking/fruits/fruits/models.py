# ------------------------------------------------------------------------------
# Pydantic types
# ==============================================================================
# > Here we turn our table models into Pydantic types
#
# Ideally we'd have an API model layer and a DATA model layer, but we're conflating
# the two in this mocking example. I guess in general they can be shared, so long
# as you're not tightly coupling your code. Remember that similar is NOT the same!
#
# Piccolo gives us a handy `create_pydantic_model` function, and we can set any
# column to `secret=True` to hide it from API responses. Very handy for fields
# like `User.id` to prevent hacks and scraping.
#
#
# Serialization
# -------------
# > @ https://docs.pydantic.dev/latest/concepts/serialization/
# > For `None` values use `exclude_none=True` or `exclude_unset=True`!
#
# - The `ID` field is hidden by default (no need for `secret=True`)
# - Use `include_default_columns=True` to include all columns
# - `create_pydantic_model` isn't great for foreign keys (unless nested)
#
# Pydantic models have a `.model_dump()` method which returns the data as a
# dictionary. This can be useful when passing in all `POST` data to a model.
# You can exclude optional missing fields with `exclude_unset=True`, and there are
# other options also.
#
# 
# Foreign keys
# ------------
# > #! It's wise to create your own Pydantic models if you're using joins!
#
# The more complex the query, the harder it is for Piccolo "magic" models.
#
#
# Flat shape -vs- nested
# ----------------------
# > #! `create_pydantic_model` only works with foreign keys for nested style,
# > so create your own Pydantic models for a flatter style (which Piccolo
# > uses by default)
# 
# At the moment you can either:
# 
# 1. Write your own Pydantic `response_model` to fit default flat shape
# 2. Use `nested=True` and `.nested()` for automatic nested Pydantic models
#     - Rather than `"color.name"` you'd get `"color" : { "name": <value> }`
#     - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/serialization/index.html#nested
#
#
# UUID
# ----
# > We're currently allowing `UUID` in our Pydantic model but setting to `None`.
#
# We then update it in the route function with a variable assignment. Alternatively,
# see `fruits.tables` -> "Secret columns" for a different approach.
#
#
# Required values
# ---------------
# > By default it seems ALL values are optional and can be `None`, but this is
# > not always acceptable: see "Unrequired values" below.
#
# - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/serialization/index.html#required-fields
#
#
# Un-required values
# ------------------
# > In one of our routes, we needn't supply the `ID` or `UUID` as these have
# > already been set (or are automatic) ...
#
# We have two options:
#
# 1. Don't supply these in the request body and use `exclude_unset=` in dump
# 2. Don't supply these in the request body and use a custom Pydantic model
#     - A `FruitsModelInWithoutUUID` with only the fields we require
#     - This would work great with `.update()` database functions!
#
#
# Data integrity
# --------------
# > SQLite defaults to accept whatever data you give it by default ...
# > @ https://sqlite.org/stricttables.html
#
# SQLite doesn't respect types unless it's a strict table. Strict tables are
# inconvenient with Piccolo as we have helpful column types (especially when
# using Postgres) ... ALWAYS validated the `DataModelIn` before inserting!
#
#
# Errors
# ------
# 1. `Any` is a bad type, is this the only thing we can use?
# 2. Our `UUID` gets automatically generated, so we don't need user to supply it.
#    - By default `create_pydantic_model` will return `None` if it's not supplied.
#    - This is fine! We can update it in the route function.
#    - Otherwise use `exclude_columns` (unlikely) or `secret=` for the return value.
#
#
# Wishlist
# --------
# 1. Add a `ColorsModelIn` model and endpoint for the `Colors` table.

from piccolo_api.crud.serializers import create_pydantic_model
from fruits.tables import Fruits, Colors
from typing import Any # (1)


# Single -----------------------------------------------------------------------
# For flat models you can use automatic Pydantic model creation. You may need to
# use `**data.model_dump(exclude_unset=True)` in some routes.

FruitsModelIn: Any = create_pydantic_model(
    table=Fruits,
    model_name="FruitsModelIn",
)

FruitsModelOut: Any = create_pydantic_model(
    table=Fruits,
    model_name="FruitsModelOut",
)


# Foreign keys -----------------------------------------------------------------
# > Piccolo returns a flat shape for foreign key joins by default.
#
# A flat shape is great for Elm Lang, but not helpful when trying to use
# `create_pydantic_model`: use a nested style if you're using that function (for
# the time being at least). Requires `.output(nested=True)` in the `.select()`.
# 
# Ideally, create your own Pydantic models for whatever you want to return!

FruitsAllModelOut: Any = create_pydantic_model(
    table=Fruits,
    model_name="FruitsAllModelOut",
    nested=True,
    include_default_columns=True,
)


