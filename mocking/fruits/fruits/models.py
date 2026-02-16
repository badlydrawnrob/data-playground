# ------------------------------------------------------------------------------
# Pydantic types
# ==============================================================================
# > See `badlydrawnrob/python-playground/building-with-fast-api` for more docs.
#
# Piccolo helps us turn our table models into Pydantic types
#
# Ideally we'd have an API model layer and a DATA model layer, but we're conflating
# the two in this mocking example. I guess in general they can be shared, so long
# as you're not tightly coupling your code. Remember that similar is NOT the same!
#
# Values are required by default (`null=False`).
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


