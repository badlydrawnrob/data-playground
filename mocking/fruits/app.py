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
# > @ https://tinyurl.com/piccolo-sqlite-tips-concurrent
#
# Piccolo automatically creates the database and schema. It also connects and
# closes the database connection as needed.
#
#
# Piccolo Admin
# -------------
# > @ https://piccolo-api.readthedocs.io/en/latest/piccolo_admin/index.html
#
# The authentication method we're using is fine for now, although Piccolo offers
# other ways to authenticate. You may also like to explore your data
# entries with Piccolo Admin (I'm using it for local only as a security measure).
#
#
# Serialization
# -------------
# > It would be wise to use `DataModelIn` layer before insertions
# 
# SQLite is not in strict mode, so potentially ANY data is permissable.
#
#
# Performance (SQL -vs- Elm)
# --------------------------
# > SQL is waaay quicker at search filters than Elm or Python so ...
# 
# - `await Task.select().where(Task.id == task_id)` ... GOOD!
# - `if list: for i in list: if i.id == task_id:`   ... BAD!
#
#
# ------------------------------------------------------------------------------
# Wishlist
# ------------------------------------------------------------------------------
# > Some of these may never get done! (YAGNI and just-in-time)
#
# 1. ⚠️ Tighten up the types?
#    - Does the API allow me to break the app? (SQLite types are too loose)
# 2. Create a script that automatically creates mock data
#    - Use `sqlite-utils` or Piccolo itself
# 3. Add SQLite transactions (see docs)
#    - Test concurrent connections and writes
#    - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/tutorials/fastapi.html#transactions
# 4. Add `UUID` for certain endpoints that are indexed
#    - We don't really need these for `Colors`
# 5. Add logging for FastApi on the production server?
#    - @ https://tinyurl.com/prep-fastapi-for-production
# 6. Understand how Piccolo apps work a bit better?
#     - @ https://piccolo-orm.readthedocs.io/en/latest/piccolo/projects_and_apps/
# 7. How best to reduce the surface area of XSS attacks?
#    - Do we need to sanitize text if it's not rendered as HTML or used in SQL?
# 8. What's the best method to insert one-to-many relationships?
#    - See the `tables.py` file for more notes.
# 9. What's affecting performance over time?
#    - Lookups with `UUID`s for example
#
#
# Questions
# ---------
# 1. When does async break with SQLite? (`.select()` + write operations)
# 2. What is best practice for response data and status codes?
# 3. How to have a high-level view of data and flow so everything makes sense?
#    - As your application grows it can be hard to understand.
# 4. Where is it better to use raw SQL instead of an ORM?
#    - At scale performance can be an issue with ORM queries.
# 5. When to use ATOMIC vs DYNAMIC routes? (Elm Spa Article forms)
#    - e.g: `/user/{id}/fruits` (POST)
#    - e.g: `/user/{id}/fruits/{fruit_id}` (ADD/DELETE, -vs- `List Int`)
# 6. When to use abstraction to reduce code duplication?
# 7. Change `.env` settings to something simpler?
#    - By default `.env` files don't handle dictionaries.
#    - You store it as a `json` string, then convert to a dictionary
# 8. ~~Are results cached?~~ (later/never)
#    - @ https://www.powersync.com/blog/sqlite-optimizations-for-ultra-high-performance

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

#! from piccolo_admin.endpoints import create_admin
from piccolo.table import create_db_tables


from fruits.piccolo_app import APP_CONFIG 
from fruits.routes import fruits_router, user_router
from fruits.tables import Colors, Fruits


# ------------------------------------------------------------------------------
# Setting up the database
# ==============================================================================
# > This part of the app can be treated like a black box. You only need to know
# > what it does, not how.
#
# 1. `create_admin` only registers the tables for the view (not create them)
# 2. `piccolo migrations forwards user` will create the `BaseUser` table
#     - @ https://tinyurl.com/baseuser-create-list-edit (CLI user functions)
# 3. `create_tables()` or `create_db_tables()` creates the DB and tables.
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
#     - @ https://fastapi.tiangolo.com/tutorial/static-files/#use-staticfiles
# 2. `Mount` is a FastAPI advanced feature (maybe not great for quickstart). The
#    current `agsi new` command uses Starlette, but possibly best to use FastAPI?
#    - @ https://fastapi.tiangolo.com/advanced/sub-applications/

app = FastAPI(lifespan=lifespan)
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
app.include_router(user_router) #! Move to it's own route file?


# Homepage ---------------------------------------------------------------------

@app.get("/")
def home():
    return RedirectResponse(url="/fruits/")