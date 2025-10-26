# README

> A fruits API using Python and the [Piccolo](https://piccolo-orm.com/) ecosystem!

This mocking example is based on Elm Land's [fruits API](https://github.com/elm-land/elm-land/tree/main/examples/06-query-parameters) to see the difference in speed and efficiency of Elm-based queries compared to SQLite and FastAPI.

1. Pick a naming convention and stick to it:
    - Singular -vs- plural (eg: column names)
    - Capital Case, Sentence case, lowercase (e.g: tags)
2. Use a business identifiers as well as incremental serial `ID`.
    - Make sure to [use indexes](https://github.com/piccolo-orm/piccolo/issues/1271#issuecomment-3395347091) for fast searching, but ...
    - Integers are approximately 1.2 times faster than bytes ...
    - About 1.4 times faster than strings during join operations.
3. **Authentication uses the `BaseUser` table** and [`BaseUser.login()`](https://piccolo-orm.readthedocs.io/en/latest/piccolo/authentication/baseuser.html#login-login-sync) function
    - **[JWT is a bad default](https://evertpot.com/jwt-is-a-bad-default/) but probably [use it anyway]**
4. Piccolo uses [seperate packages](https://github.com/piccolo-orm/piccolo/issues/1272) for it's Admin and API.
    - Ideally you could `uv add 'piccolo-api[sqlite]'` and `scaffold --fastapi`
    - It might be wise to host `piccolo-admin` only locally for extra security
5. You can check SQLite column data types in a [few ways](https://database.guide/5-ways-to-check-a-columns-data-type-in-sqlite/)
    - SQLite [data types](https://www.sqlite.org/datatype3.html) are really quite simple
    - Piccolo stores `json` as `text` (I think)
6. Should API models and DATA models be totally separate (requires a little more work)


## Database

> Currently the master `.config/git/ignore` file disallows `*.sqlite` databases

This is probably a LOT better for security reasons, so make sure you backup and have an easy way to setup your initial data.


## Coding style

> In general prefer a data-style rather than OOP

Aim to write your functions in Elm style as much as possible, which isn't mutable. Don't force Python to do what it's not meant to do, however. Maybe objects are OK when used in moderation.

I imagine OCaml and Elm would do things manually, rather than using magic like `response_model=` and `model_dump()`?


## Dependencies

> A big concern is having too many dependencies!

Just keep an eye on how fast these are changing and what impact it has on your maintenance.


## Models

> Currently I'm using `create_pydantic_models` and not _quite_ splitting API and DATA layer

Unless the API and DATA layer models need to vary, generating a single model that can be reused for `DataModelIn` and `DataModelOut` might work ok. FastAPI will check it for data integrity in `data: Request` and `response_model=`.


## Bugs

### Pylance squiggles

Is this because `pyproject.toml` is `name="fruits"` and I also have a fruits subfolder?

### Naming conventions

> Have a naming convention and stick to it: singular or plural?

- Table `Fruit` or `Fruits`?
- Model `FruitModelIn` or `FruitsModelIn`?
- Folder `fruit` or `fruits`? (package)

### 🤖 Ai fails hard

> Trying to understand `lifespan` and `contextlib` was a big fat fail!

- [Using LLMs](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) for coding
- Be extremely careful letting Ai handle critical parts of your app (human in the loop)

### Pydantic models for foreign keys

It seems [easier](https://github.com/piccolo-orm/piccolo/issues/1292) to just create your own flat-style Pydantic model!

### Pydantic `null` values

- [An issue here](https://github.com/piccolo-orm/piccolo/issues/1132)


## SQLite

> Piccolo is one of the easiest ways to query your data (see [ORM challenges](https://piccolo-orm.com/blog/orm-design-challenges/))

- Peewee was great but not setup for `async` (although it has an [untested plugin](https://peewee-async.readthedocs.io/en/latest/index.html))
- SQLModel is an abstraction of an abstraction (SQLAlchemy) and feels bloated to me

SQLModel uses the Data Mapper pattern rather than Active Record and is a little more confusing with `.session.exec()`, add, commit, etc, whereas Piccolo needs no `connect()` or `close()` functions as it's `select()` queries are handled automatically. Peewee and Piccolo have an object oriented style, but (I think) only Piccolo has a functional data style. Piccolo feels a lot lighter and easier to wrap your head around!

The downside of using SQLite over Postgres is data integrity (without [strict tables](https://www.sqlite.org/stricttables.html)) and data types. Some SQLite fields are stored as `json`, which will require a [plugin](https://sqlite.org/json1.html) to query them, or use [`sqlite-utils`](https://sqlite-utils.datasette.io/en/stable/cli-reference.html) (with `--json-cols`) and `jq`.
    
The upsides are Piccolo gives a wider range of [columns](https://piccolo-orm.readthedocs.io/en/latest/piccolo/schema/column_types.html) to work with, so whereas SQLite only has `1` (`True`) and `0` (`False`) for boolean values, Piccolo will add them as [proper (`json`)](https://github.com/piccolo-orm/piccolo/issues/1257) types. You also have to be careful with [empty `String`](https://github.com/piccolo-orm/piccolo/issues/353) values.

Postgres is _far_ more capable than SQLite but is also harder to setup, store, and migrate data (it's documentation is huge).


## User experience

> See the "Van Man Problem" for API architecture and design.

1. `Delete` operations should always prompt the user to confirm.
2. Handle errors correctly. Don't leak sensitive information.
3. Authenticate all routes that require authentication, or are "risky".
    - Make sure it's the correct user that is allowed to edit their posts.
4. What data should be public? What data should be private?
