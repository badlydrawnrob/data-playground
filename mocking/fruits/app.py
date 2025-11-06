# ------------------------------------------------------------------------------
# Fruits demo app (Piccolo ORM)
# ==============================================================================
# > Treat some parts of the app as a "black box" and stick to your learning frame
#
# 1. FastApi with models and routes (API layer)
# 2. Piccolo ORM (async data layer) for CRUD operations
#    - Peewee isn't setup for async @ https://charlesleifer.com/blog/asyncio/
# 3. Best practices for REST APIs (some things don't have a standard)
#    - @ https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api
#
# It seems best to split out the API layer from the DATA layer, so each could be
# swapped out independently (SQLModel is too tightly connected). Changing ORMs
# and databases can be tricky and time consuming! There's too much to learn, so
# aim for "just in time" learning. What's not my job?
#
#
# Learning frame
# --------------
# 1. ✅ Static typed functional python where it makes sense (rrr classes, Elm style)
# 2. ✅ Simple and minimal data structures with a simple API (rrr file size)
# 3. ✅ Immutable data, no `None` values, minimal `try/except/finally` blocks 
# 3. ✅ Understanding API route architecture decisions (# of endpoints)
# 4. ✅ Understanding backend data structures (especially search queries)
# 5. ✅ Aiming to keep data shapes flat where possible (avoid nesting?)
# 6. ✅ Remove code duplication. Simplify your code. 5 steps (Tesla)
# 7. ✅ Maximise readability and maintainability (my stupid future self)
#
# 1. ❌ ~~Security: authentication and more~~
#     - is owner of data, is logged on, etc
#     - Malicious SQL injections and DDOS attacks.
#
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
# SQLite transactions
# -------------------
# > Always use a `DataModelIn` before saving to SQLite as it's not strict.
#
# 1. Async transactions can fail if you `select()` followed by a write.
#     - Be very careful and use the correct transaction type where needed.
#     - @ https://tinyurl.com/piccolo-sqlite-and-asyncio
#     - @ https://github.com/piccolo-orm/piccolo/discussions/1247
# 2. SQL is waaay quicker at search filters than Elm or Python so ...
#    - `await Task.select().where(Task.id == task_id)` ... GOOD!
#    - `if list: for i in list: if i.id == task_id:`   ... BAD!
#
#
# Improvements
# ------------
# 1. Aim for beautiful, readable, ELi5 code (my stupid future self)
#     - I shouldn't need to be an expert to understand Piccolo!
#     - Elm code uses a lot of whitespace which I prefer
#     - If something can be simplified or removed, do so
# 2. Do not include needless packages where they can be avoided
#     - Code and dependencies should follow a miniamlist approach
# 3. Code should be pitched at the right level of ability and knowledge
#     - Advanced features should be hidden for begginers (like `Readable`)
# 4. Code should follow expectations setup from other parts of the documentation
#     - `playground run` is using a `Band` database, so why not here?
# 5. Aim for faster loading while still sticking to the above
#     - Which code is faster in an object oriented style? (e.g: find task with id)
#     - If speed is negligible, prefer readable and functional style
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
# Errors
# ------
# 1. Tighten up the types?
# 2. SQLiteEngine has no `connect()` and `close()` functions?
#     - This should be documented somewhere.
#
#
# Wishlist
# --------
# > Some of these may never get done! (YAGNI and just-in-time)
#
# 1. Create a script that automatically creates mock data
#    - Use `sqlite-utils` or Piccolo itself
# 2. Add SQLite transactions (see docs)
#    - Test concurrent connections and writes
#    - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/tutorials/fastapi.html#transactions
# 3. Understand how Piccolo apps work a bit better?
#     - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/projects_and_apps/
# 4. Decide whether to persue Migrations or just use JQ and `sqlite-utils`
#    - Migrations are a little advanced for beginners
#    - Auto migrations do not work with SQLite
# 5. How best to reduce the surface area of XSS attacks?
#    - Do we need to sanitize text if it's not rendered as HTML or used in SQL?
# 6. What's the best method to insert one-to-many relationships?
#    - See the `tables.py` file for more notes.
# 7. Harden validating fields and routes ...
#    - Fields are not empty and not null, for example


from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from piccolo_admin.endpoints import create_admin
# from piccolo_api.crud.endpoints import PiccoloCRUD
# from piccolo_api.fastapi.endpoints import FastAPIWrapper
from piccolo.table import create_db_tables


from fruits.piccolo_app import APP_CONFIG 
from fruits.routes import fruits_router
from fruits.tables import Colors, Fruits


# ------------------------------------------------------------------------------
# Setting up the database
# ==============================================================================
# > This part of the app can be treated like a black box. You only need to know
# > what it does, not how.
#
# 1. `create_admin` only registers the tables for the view (not create them)
# 2. `create_tables()` or `create_db_tables()` creates the DB and tables.
#
# 
# Migrations
# ----------
# > I feel like this is an advanced topic and there's other ways to do it.
# 
# SQLite does not have automatic migrations currently. Use `sqlite-utils`.
#
#
# 🤖 Ai summary: What the fuck is a context manager?
# --------------------------------------------------
# > @ https://medium.com/@marcnealer/fastapi-after-the-getting-started-867ecaa99de9
#
# It ensures that setup (like opening a file) happens when you start using the resource,
# and cleanup (like closing the file) happens when you're done, even if an error occurs.
#
# - What exactly should be setup on startup? Shutdown?
# - The essential is to create our database and setup the tables.
#
# I've not come across this the Elm world and the `contextlib` docs really don't
# do a great job of explaining it, or why I should care. In fact I find the whole
# concept of `async` a little weird, scattering around `async` and `await` keywords
# all over the place. It feels like it should be built into the language.
#
#
# 🤖 Ai summary: `yield`
# ----------------------
# > The lifespan allows us to define startup and teardown in one function
#
# The code block before the yield executes during the startup phase, just before
# the application begins to accept requests. This is where you can perform expensive
# operations like loading a model or establishing a database connection. The yield
# acts as a pause point, after which the application becomes operational and can
# handle incoming requests. The code block after the yield executes during the
# shutdown phase, after the application has finished processing all requests.
#
#
# 🤖 Ai fails
# -----------
# It took an unnecessary amount of time to understand lifespan etc. It's easier
# than the web would have you believe, but there's not many ELi5 resources. Do
# not attempt to use Ai to do this for you, as it gave me a MASSIVE and WRONG
# code sample, even though it crawled the Piccolo docs, which goes to show it can't
# (yet) be trusted for critical tasks. Does this mean the docs need improving?
# At least for a bot to crawl them.

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_tables(Colors, Fruits, if_not_exists=True)
    yield


# ------------------------------------------------------------------------------
# Initiate the app (with Piccolo Admin)
# ==============================================================================
# > We're extending `FastAPI` here to add Piccolo's Admin interface
#
# 1. `StaticFiles` does NOT serve static files by default (why not?!) so you've
#     got to explicitly tell it to. We're using the fastapi package (not starlette)
# 2. `Mount` is a FastAPI advanced feature (maybe not great for quickstart). The
#    current `agsi new` command uses Starlette, but possibly best to use FastAPI?
#    - @ https://fastapi.tiangolo.com/advanced/sub-applications/
# 3. It seems `create_admin` function automatically creates the tables?
#    - If so `@asynccontextmanager` above is not needed?
#    - I'm not super keen on the `tables=` argument. Better to be explicit and
#      list all tables here? Do we _really_ need `APP_CONFIG` at all?
#
# Piccolo Admin
# --------------
# > #! Make sure to protect your admin routes in production! `allowed_hosts=`
#
# Static files
# -------------
# > @ https://fastapi.tiangolo.com/tutorial/static-files/#use-staticfiles

app = FastAPI(lifespan=lifespan)

admin = create_admin(tables=APP_CONFIG.table_classes)

app.mount("/admin", admin)
app.mount("/static", StaticFiles(directory="static"), name="static")


# Middleware -------------------------------------------------------------------

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


# Routes and tabs ---------------------------------------------------------------

app.include_router(fruits_router, prefix="/fruits") # Swagger and `/redoc` groups


# Homepage ---------------------------------------------------------------------

@app.get("/")
def home():
    return RedirectResponse(url="/fruits/")