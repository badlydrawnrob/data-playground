from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from piccolo_api.crud.endpoints import PiccoloCRUD
from piccolo_api.fastapi.endpoints import FastAPIWrapper
from piccolo.table import create_db_tables_sync

from models.database import Fruits, Colours

# from routes.fruits import fruits_router

import uvicorn

# ------------------------------------------------------------------------------
# Fruits demo app (Piccolo ORM)
# ==============================================================================
# > Treat some parts of the app as a "black box" and stick to your learning frame
#
# 1. FastApi with models and routes (API layer)
# 2. Piccolo ORM (async data layer) for CRUD operations
#    - Peewee isn't setup for async @ https://charlesleifer.com/blog/asyncio/
#
# It seems best to split out the API layer from the DATA layer, so each could be
# swapped out independently (SQLModel is too tightly connected). Changing ORMs
# and databases can be tricky and time consuming! There's too much to learn, so
# aim for "just in time" learning. What's not my job?
#
# My job
# ------
# 1. Static typed functional python where it makes sense (rrr classes, Elm style)
# 2. Simple and minimal data structures with a simple API (rrr file size)
# 3. Understanding API route architecture decisions (# of endpoints)
# 4. Understanding backend data structures (especially search queries)
# 5. Aiming to keep data shapes flat where possible (avoid nesting?)
# 6. Remove code duplication. Simplify your code. 5 steps (Tesla)
# 7. Maximise readability and maintainability (my stupid future self)
#
# Not my job
# ----------
# 1. ~~Security: authentication and more~~
#     - is owner of data, is logged on, etc
#     - Malicious SQL injections and DDOS attacks.
#
# Piccolo ORM
# -----------
# 1. Piccolo by default uses `engine_finder` from `piccolo_conf.py`
# 2. Piccolo can automatically create tables from your models
#    - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/query_types/create_table.html
# 3. Piccolo connects and closes database with a single function (careful with async writes)
#    - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/tutorials/fastapi.html#transactions
#    - @ https://tinyurl.com/piccolo-sqlite-tips-concurrent (database locked error)
#
#
# Questions
# ---------
# 1. Do we need `@app.on_event("startup")` or `lifespan` event handlers?
#    - How does Piccolo handle setting up the database?
# 2. When does async break with SQLite? (`.select()` + write operations)
# 3. How to have a high-level view of data and flow so everything makes sense?
#    - As your application grows it can be hard to understand.
# 4. Are `id` fields handled automatically by Piccolo?
# 5. Where is it better to use raw SQL instead of an ORM?
#    - At scale performance can be an issue with ORM queries.
# 6. Where to use `PUT` vs `PATCH` requests? (all data or some data)
# 7. When to use ATOMIC vs DYNAMIC routes? (Elm Spa Article forms)
#    - e.g: `/user/{id}/fruits` (POST)
#    - e.g: `/user/{id}/fruits/{fruit_id}` (ADD/DELETE, -vs- `List Int`)
# 8. Are `Int` id joins faster than `String` joins? (email as id)
# 9. When to use abstraction to reduce code duplication?
# 10. ~~Are results cached?~~ (later/never)
#    - @ https://www.powersync.com/blog/sqlite-optimizations-for-ultra-high-performance
# 11. Avoid admin routes? (make sure Piccolo admin is protected)
#    - ~~@ https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/~~
# 12. Potentially use SQLite Utils to easily setup mock data?
# 13. Consider different `include_router` packages for authentication routes?
#    - @ https://fastapi.tiangolo.com/tutorial/bigger-applications/
#    - @ https://stackoverflow.com/a/67318405
# 14. Add logging for FastApi on the production server?
#    - @ https://tinyurl.com/prep-fastapi-for-production
# 15. Change `.env` settings to something simpler?
#    - By default `.env` files don't handle dictionaries.
#    - You store it as a `json` string, then convert to a dictionary
#
#
# Wishlist
# --------
# 1. Better documentation for SQLite and `engine_finder()`
#    - Setup with FastAPI
#    - Setup database, opening and closing connections, and so on.
#    - Does SQLite have connection pooling?


app = FastAPI()


# Register our routers ---------------------------------------------------------

app.include_router(fruits_router, prefix="/fruits")


# Middleware -------------------------------------------------------------------
# A list of allowed CORS origins (defaults to only same domain and port)
# @ https://fastapi.tiangolo.com/tutorial/cors/

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Database setup and build -----------------------------------------------------

@app.on_event("startup")
def on_startup():
    create_db_tables_sync(Colours, Fruits, if_not_exists=True)


# Routes -----------------------------------------------------------------------

@app.get("/")
def home():
    return RedirectResponse(url="/fruits/")


# Run our app ------------------------------------------------------------------
# Slightly different from the "Building with FastAPI" book code sample

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
