# ------------------------------------------------------------------------------
# Pydantic types
# ==============================================================================
# > See `badlydrawnrob/python-playground/building-with-fast-api` for more docs.
#
# Piccolo turns our table models into Pydantic types with `create_pydantic_model`.
# Ideally we'd have both API models and DATA models to assure strict types added
# with SQLite (which isn't in strict table mode). Take care with inserts.
#
# ------------------------------------------------------------------------------
# WISHLIST
# ------------------------------------------------------------------------------
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
#
# > Flat shape by default
# 
# You may need to use `**data.model_dump(exclude_unset=True)`

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
# 
# > As complexity increases, it's better to create custom Pydantic models.
#
# Flat shape is great for Elm Lang, but not helpful when trying to use Piccolo's
# `create_pydantic_model` function with foreign keys. A nested shape is much easier
# to work with, but requires `.output(nested=True)` in the `.select()`.

FruitsAllModelOut: Any = create_pydantic_model(
    table=Fruits,
    model_name="FruitsAllModelOut",
    nested=True,
    include_default_columns=True,
)


