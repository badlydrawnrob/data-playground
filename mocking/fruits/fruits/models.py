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
#
# Pydantic models have a `.model_dump()` method which returns the data as a
# dictionary. This can be useful when passing in all `POST` data to a model.
# You can exclude optional missing fields with `exclude_unset=True`, and there are
# other options also.
#
#
# Flat shape -vs- nested
# ----------------------
# > By default Piccolo returns a flat shape for foreign keys, which is Elm Lang's
# > preference too. You can use `nested=True` to get a nested shape.
#
# - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/serialization/index.html#nested
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
# > By default it seems ALL values are optional and can be `None`
#
# - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/serialization/index.html#required-fields
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

from piccolo_api.crud.serializers import create_pydantic_model
from fruits.tables import Fruits, Colors
from typing import Any # (1)


# Single -----------------------------------------------------------------------

FruitsModelIn: Any = create_pydantic_model(
    table=Fruits,
    model_name="FruitsModelIn",
)

#! We don't need `include_default_columns` anymore
FruitsModelOut: Any = create_pydantic_model(
    table=Fruits,
    model_name="FruitsModelOut",
    # include_columns=(Fruits.color.name, Fruits.colors.background, Fruits.name),
)

ColorsModelIn: Any = create_pydantic_model(
    table=Colors,
    model_name="ColorsModelIn",
)

# Multiple ---------------------------------------------------------------------
# 1. Here's a nested example. It automatically creates foreign key models:
#    - `.output(nested=True)` in the route function

FruitsAllModelOut: Any = create_pydantic_model(
    table=Fruits,
    model_name="FruitsAllModelOut",
    nested=True,
    include_default_columns=True,
)


