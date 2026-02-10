# ------------------------------------------------------------------------------
# Pydantic types
# ==============================================================================
# > Piccolo helps us turn our table models into Pydantic types
#
# Ideally we'd have an API model layer and a DATA model layer, but we're conflating
# the two in this mocking example. I guess in general they can be shared, so long
# as you're not tightly coupling your code. Remember that similar is NOT the same!
#
#
# Serialization
# -------------
# > See Piccolo and Pydantic on serialization docs. In general it's best to create
# > your own custom Pydantic models, as Piccolo "magic" falls down eventually.
# 
#     @ https://docs.pydantic.dev/latest/concepts/serialization/
#     @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/serialization/index.html
#
# 1. Primary keys `null=False` by default (but Foreign Keys `null=False`)
# 2. Primary keys are hidden by default in the response (`secret=True`)
# 3. `model_dump(exclude_unset=True)` is useful for optional fields
#
#
# Flat shape -vs- nested
# ----------------------
# > `create_pydantic_model` works best with foreign keys in a nested style.
# > @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/serialization/index.html#nested
# 
# 1. Without the `nested=True` setting you get the default flat shape.
# 2. More complicated models fall down with this "magic"; create your own.
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
# Required values
# ---------------
# > See `/tables.py` for optional and required fields. If `null=False`, the field
# > should be required! `UUID` field (if primary key) is auto-generated.
#
# - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/serialization/index.html#required-fields
#
#
# Errors
# ------
# > See `badlydrawnrob/python-playground/building-with-fast-api` for more docs.
#
#
# Wishlist
# --------
# 1. Add a `ColorsModelIn` model and endpoint for the `Colors` table.
# 2. Add a `default_factory` setting with custom `Fruits` model for `UUID`?
# 3. Check if field can be `None` in Pydantic model when it shouldn't be? 

from fruits.tables import Fruits, Colors
from pydantic import BaseModel
from piccolo.utils.pydantic import create_pydantic_model
from typing import Any # (1)


# User -------------------------------------------------------------------------

class TokenResponse(BaseModel):
    access_token: str
    token_type: str


# Single -----------------------------------------------------------------------
# For flat models you can use automatic Pydantic model creation. You may need to
# use `**data.model_dump(exclude_unset=True)` in some routes.

FruitsModelIn: Any = create_pydantic_model(
    table=Fruits,
    model_name="FruitsModelIn",
    exclude_columns=(Fruits.id,) # Auto-UUID in table
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


