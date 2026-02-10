# README

> A fruits API using Python and the [Piccolo](https://piccolo-orm.com/) ecosystem!

This mocking example is based on Elm Land's [fruits API](https://github.com/elm-land/elm-land/tree/main/examples/06-query-parameters) to see the difference in speed and efficiency of Elm-based queries compared to SQLite and FastAPI.

## Versions

1. [Fruits API](https://tinyurl.com/fruits-api-0f2caad) with basic routes and no authentication
2. Fruits API with basic routes and authentication
3. Fruits API with query routes and authentication


## Conventions

1. Public `UUID` business identifier (auto-indexed)[^1]
2. Use Serial `ID`s (or bytes) when possible, both are faster than `String`!
3. JWT for authentication only, `/profile` endpoint for preferences[^2]
4. Piccolo already has a `BaseUser` and `BaseUser.login()` function
5. Piccolo Admin is potentially a security risk (use offline only?) 
6. Piccolo API and Admin don't need to be used, they're handy packages
7. Piccolo stores values as `Int` or `Text` with SQLite (even `json`)
8. Use `create_pydantic_models` sparingly and roll your own Pydantic types
9. Split API models from Data models wherever possible (not complected)
10. Avoid unecessary endpoints that could become a security risk


## Setup

> After running these commands, insert values into database.
> Add `Colors` first as it's a foreign key `Fruits.colors` (see `sqlite-utils.sql`).

We don't need to worry about user creation or hashing passwords, but currently we
set them up manually (rather than in-app). We can eventually build in `BaseUser.create_user()` when ready.

```bash
# Run the app (and create DB)
# Populate the database with `sqlite_utils.sql`
uv run main.py

# Setup the user table
piccolo migrations forwards user

# Create the user (see `bruno/collection.bru`
# for user details to use with CLI command)
piccolo user create

# Login and create JWT token (or use Bruno)
# `client_id` and `client_secret` not set!
curl -X 'POST' \
'http://localhost:8000/login' \
-H 'accept: application/json' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=password&username=[USER]&password=[PASSWORD]&scope=&client_id=none&client_secret=none'
```


## To Do

> Handle all errors "just-in-time" but use logs and screenshots/123s so you can
> replicate the bug. Make sure to use logs and test the API with Bruno for correct
> and incorrect data.

1. Transactions can be avoided by using writes only (faster queries).
    - It's helpful to understand _why_ transactions _would_ be needed ... when
      read and write operations are housed in the same endpoint/transaction.
    - Transactions are `DEFFERED` by default (`IMMEDIATE` is required if read
      and writes are used together). Always test concurrent connections.
    - `RETURNING` statement is essential if using writes only, as we need to make
      sure that a row exists (otherwise we'd need `EXISTS` and a `SELECT`).
    - If requiring `IMMEDIATE`, read "Using SQLite and Asyncio effectively"
      and (ideally) use `dependencies=[Depends(transaction)]` in the endpoint.
2. Should `timeout` always be used with SQLite?
    - https://piccolo-orm.readthedocs.io/en/latest/piccolo/tutorials/using_sqlite_and_asyncio_effectively.html#timeout
3. Naming conventions:
    - `Fruit` -vs- `Fruits`
    - `FruitModelIn` or `FruitsModelIn`?
    - `/fruits` folder or `/fruit`?
    - `["Capital", "Case"]` -vs- `["lower", "case"]`
    - And so on ...
4. Run a speedtest on all backend endpoints as well as frontend
    - You can use bombardier for API concurrent connections.
5. Populate database with `sqlite-utils` (migrations are confusing)
    - colors and fruits defaults
    - Auto migrations do not work with SQLite
6. Prefer custom Pydantic models ...
    - Are we happy with a flat `json` response?
    - Or stick to a nested one?
7. `BaseUser` is a little bit awkward to extend with a `UUID` field
    - Can we extend it properly without a `Profile` column?
    - Or simply use the `username` and forgo the `UUID`?
8. Assure that data integrity and types are maintained with SQLite
    - It can fall over in [some circumstances](https://github.com/piccolo-orm/piccolo/discussions/1247) without strict tables or pydantic!
9. Add in [piccolo admin](https://github.com/piccolo-orm/piccolo_admin)?
    - Currently not included in our Python packages
    - Used in `app.py` and `piccolo_conf.py`
10. Fix larger comments with Pep 8?
    - Longer `#` comments could use `"""` docstrings.
11. `create_pydantic_model` requires the `piccolo-api` package
    - Just create my own models in future?
12. Check the "APIs you won't hate" book on standard return values
    - What [should be returned](https://softwareengineering.stackexchange.com/questions/314066/restful-api-should-i-be-returning-the-object-that-was-created-updated) from a `Update`, `Delete`, ..., in a REST API?


## Performance

1. Aim for atomic transactions rather than bulk
    - You can always do bulk inserts/edits with `sqlite-utils`
2. It might reduce errors to increase [`timeout`](https://github.com/piccolo-orm/piccolo/issues/687) value in SQLite
3. Using a single `update()` statement instead of a read then write
    - Always use the `.returning()` method or [bugs](https://github.com/piccolo-orm/piccolo/issues/1319) can appear.
4. Use [Bombardier](https://github.com/codesenberg/bombardier) to stress-test your server


## Storytelling

> How you sell your thing matters ... why should they care?

Evan Czaplicki's [talk](https://www.deconstructconf.com/2017/evan-czaplicki-on-storytelling) about communicating clearly your vision and why anybody should care (when perspectives differ). Quite useful for documentation, Quick Start guides, and writing in general. Piccolo is great, but there's areas in the writing (and onboarding) for improvement.


## Database

> Currently the master `.config/git/ignore` file disallows `*.sqlite` databases

This is probably a LOT better for security reasons, so make sure you backup and have an easy way to setup your initial data.


## Coding style

> In general prefer a data-style rather than OOP

Aim to write your functions in Elm style as much as possible (which isn't mutable). Don't force Python to do what it's not meant to do, however. Maybe objects are OK when used in moderation. I imagine OCaml and Elm would do things manually, rather than using magic like `response_model=` and `model_dump()`?

Other slight weirdness is that `Fruits.insert(Fruits(**data.model_dump()))` can insert multiple values, so we're using an inner `Fruits()` object here. Conversely, `Fruits.update()` does not require this and you can supply it a record directly (it's only updating a single entry).


## Dependencies

> A big concern is having too many dependencies!

Just keep an eye on how fast these are changing and what impact it has on your maintenance.


## User experience

> See the "Van Man Problem" for API architecture and design.

1. `Delete` operations should always prompt the user to confirm.
2. Handle errors correctly. Don't leak sensitive information.
3. Authenticate all routes that require authentication, or are "risky".
    - Make sure it's the correct user that is allowed to edit their posts.
4. What data should be public? What data should be private?


## Security

> You're not Facebook. Or Google. Only build what you need.

Aim for speed and ease of reading, but take care with security. I don't _really_ need a fully functioning JWT [with claims](https://github.com/piccolo-orm/piccolo/discussions/1277) like Auth0, only a secure way for a user to login and validate their routes. Only include a `UUID` in the `payload` (it's public anyway) and an expiry date. Anything else can be retrieved once logged in from a `/profile` endpoint and cached in `localStorage` if needed.

`HS256` is fine if you own the stack and aren't sharing the `SECRET` with anyone else. For working with 3rd party JWTs, you'll need to use a `RS256` public key, or supply that to a client you don't control (if you're supplying the JWT). The JWT should ideally be used as authoration/access only — not data storage (which could reveal personal information).

Some services use tokens as a method of avoiding database or other lookups, but that only matters at scale; for a small service hitting an extra `/profile` endpoint won't make a difference in speed. Some systems use it to provide permissions like scopes (see Auth0). Again, it's too early to worry about that stuff.

Build simply. Don't overplan. YAGNI!


## Models

> Currently I'm using `create_pydantic_models` and not _quite_ splitting API and DATA layer

Unless the API and DATA layer models need to vary, generating a single model that can be reused for `DataModelIn` and `DataModelOut` might work ok. FastAPI will check it for data integrity in `data: Request` and `response_model=`.


## Bugs

For now, unless it's a blocking problem, just LOG it and move on. Find a workaround, unless it's essential to what you need to complete. You've raised a lot of issues.

### Pylance squiggles

Is this because `pyproject.toml` is `name="fruits"` and I also have a fruits subfolder?

### Naming conventions

> Have a naming convention and stick to it: singular or plural?

### 🤖 Ai fails hard

> Trying to understand `lifespan` and `contextlib` was a big fat fail!

- [Using LLMs](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) for coding
- Be extremely careful letting Ai handle critical parts of your app (human in the loop)

### Pydantic models for foreign keys

It seems [easier](https://github.com/piccolo-orm/piccolo/issues/1292) to just create your own flat-style Pydantic model!

### Pydantic `null` values

- [An issue here](https://github.com/piccolo-orm/piccolo/issues/1132)

## Piccolo documentation

- [Contributing](https://github.com/piccolo-orm/piccolo/issues/1274#issuecomment-3395426315) if you find any areas of improvement.


## SQLite

> Piccolo is one of the easiest ways to query your data (see [ORM challenges](https://piccolo-orm.com/blog/orm-design-challenges/))

- Peewee was great but not setup for `async` (although it has an [untested plugin](https://peewee-async.readthedocs.io/en/latest/index.html))
- SQLModel is an abstraction of an abstraction (SQLAlchemy) and feels bloated to me

SQLModel uses the Data Mapper pattern rather than Active Record and is a little more confusing with `.session.exec()`, add, commit, etc, whereas Piccolo needs no `connect()` or `close()` functions as it's `select()` queries are handled automatically. Peewee and Piccolo have an object oriented style, but (I think) only Piccolo has a functional data style. Piccolo feels a lot lighter and easier to wrap your head around!

The downside of using SQLite over Postgres is data integrity (without [strict tables](https://www.sqlite.org/stricttables.html)) and data types. Some SQLite fields are stored as `json`, which will require a [plugin](https://sqlite.org/json1.html) to query them, or use [`sqlite-utils`](https://sqlite-utils.datasette.io/en/stable/cli-reference.html) (with `--json-cols`) and `jq`.
    
The upsides are Piccolo gives a wider range of [columns](https://piccolo-orm.readthedocs.io/en/latest/piccolo/schema/column_types.html) to work with, so whereas SQLite only has `1` (`True`) and `0` (`False`) for boolean values, Piccolo will add them as [proper (`json`)](https://github.com/piccolo-orm/piccolo/issues/1257) types. You also have to be careful with [empty `String`](https://github.com/piccolo-orm/piccolo/issues/353) values.

Postgres is _far_ more capable than SQLite but is also harder to setup, store, and migrate data (it's documentation is huge).




[^1]: Also an option is using _both_ `UUID` (or short uuid) _and_ a primary key (`Serial`) on which to do lookups and joins. The UUID would be public-facing and the primary key private. The downside is it may require an extra `select()` to grab the primary key.

[^2]: Some say that JWT [is a bad default](https://evertpot.com/jwt-is-a-bad-default/) but I'm going to use it anyway! We also don't currently have a `client_secret`.