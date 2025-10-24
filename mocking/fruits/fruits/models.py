# ------------------------------------------------------------------------------
# Pydantic types
# ==============================================================================
# > Here we turn our table models into Pydantic types
#
# It's generally best to separate API layer models from DATA models, as sometimes
# they'll need to differ. However, Piccolo allows your tables to have secret
# columns (`Varchar(secret=True)`) in your tables, so data like `User.id` can be
# hidden from API responses. You can then use `create_pydantic_model`.
#
#
# Serialization
# -------------
# > @ https://docs.pydantic.dev/latest/concepts/serialization/
# > For `None` values use `exclude_none=True` or `exclude_unset=True`!
#
# Pydantic models have a `.model_dump()` method which returns the data as a
# dictionary. This can be useful when passing in all `POST` data to a model.
# You can exclude optional missing fields with `exclude_unset=True`, and there are
# other options also.
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
# Notes
# -----
# 1. Our `UUID` gets automatically generated, so we don't need user to supply it.
#    - `FruitsModelIn.url = None` by default, so we've just removed it
#    - Instead we can keep the `None` value and simply overwrite it ...
#    - `FruitsModelIn.id` is handled this way with `Serial()` (auto-added to DB)
#     
#
# We could also create a custom Pydantic model with `default_factory` here.
#
#
# Errors
# ------
# 1. `Any` is a bad type, is this the only thing we can use?

from piccolo_api.crud.serializers import create_pydantic_model
from fruits.tables import Fruits, Colors
from typing import Any # (1)


FruitsModelIn: Any = create_pydantic_model(
    table=Fruits,
    model_name="FruitsModelIn",
    exclude_columns=(Fruits.url,) # (1)
)

#! Should these be inside the tables.py file?
FruitsModelOut: Any = create_pydantic_model(
    table=Fruits,
    include_default_columns=True,
    model_name="FruitsModelOut",
)

ColorsModelIn: Any = create_pydantic_model(
    table=Colors,
    model_name="ColorsModelIn",
)
