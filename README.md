# README

> A soft play area for data!

## Goals

> 1. Very light data analysis
> 2. Very small app prototyping
> 3. Storing Marketing/Ads data

Examples such as the **Programming Flashcards App**, **Google Ads**, **Simple Analytics** research, **Library Data**, and so on. Should involve basically ZERO database admin, unless absolutely necessary.


## SQLite (and SQL)

> An sqlite [cheat sheet](https://vhernando.github.io/sqlite3-cheat-sheet) ...
> - [Appropriate uses for SQLite](https://www.sqlite.org/whentouse.html)
> - When to use [Postgres -vs- SQLite](https://www.boltic.io/blog/postgresql-vs-sqlite)
> - [Modern SQL](https://modern-sql.com/) and what's changed

```sql
/* Launch sqlite */
sqlite3 database.sqlite

/* Schema information */
.schema --indent
.schema Table --indent

/* Table information (orm) */
pragma table_info(Table);
pragma table_xinfo(Table);

/* Index information */
pragma index_info|list(table);

/* Column types (real) */
select typeof(Column) from Table
limit 1;

/* Clear lines */
.shell clear

/* Quit sqlite */
.quit
.exit
```

### Handy settings

> [Save SQLite settings](https://stackoverflow.com/a/42910299) in `~/.sqliterc`

```sql
-- Show table headings and column format
.headers on
.mode column
```


### Cleanup

> To save space remove all unecessary folders once you're done.

```bash
# Delete the environment (use `uv sync` to restore)
rm -rf .venv && rm uv.lock

# Check the command before running it (delete all cache folders)
find . -type d -name "__pycache__" | wc -l
find . -type d -name "__pycache__" -exec echo rm -r {} \; # `-f` is dangerous!

# Run the command (add the `-v` flag to show all files deleted)
find . -type d -name "node_modules" -exec echo rm -r {} \;
```


## Tools

> True as of 2025. There are lots of frameworks for dealing with data ...

Python isn't the ideal language for performant data transfer, but it's quite easy to get started with. Other languages like [Ocaml](https://aantron.github.io/dream/), [Elixir](https://www.phoenixframework.org/)/Go/Gleam/Roc, might be worth a look at some point (other [popular languages](https://survey.stackoverflow.co/2024/technology) here). Remember the "sunk cost fallacy" and "opportunity cost" and cognitive load it takes to learn a new thing. Is the performance 10x better? Worthy of investing 3 months of your time?

### GUIs

- [5 best GUIs](https://turso.tech/blog/5-best-free-sqlite-gui) for SQLite (and [Tad](https://www.tadviewer.com/) for pivots)
- [Enso](https://help.enso.org/) (data prep and visualisation)
- [Mockaroo](https://www.mockaroo.com/) (generate mock data)

### ORMs

> There's [async](https://www.youtube.com/watch?v=GSiZkP7cI80) and sync and not all ORMs will work for async.

- [Piccalo](https://piccolo-orm.com/) works well with FastApi (careful with [types](https://github.com/piccolo-orm/piccolo/issues/1187) and [async](https://piccolo-orm.readthedocs.io/en/1.3.2/piccolo/tutorials/using_sqlite_and_asyncio_effectively.html) writes)
- [Peewee](https://docs.peewee-orm.com/en/latest/) is great (`sync` only with [these](https://docs.peewee-orm.com/en/latest/peewee/database.html#framework-integration) API frameworks)
- [Records: SQL for humans](https://github.com/kennethreitz/records) for raw SQL (alternative to `sqlite-utils` with `.csv` etc)
- [Ice axe](https://github.com/piercefreeman/iceaxe) could be one for the future (Postgres only)
- A list of other ORM options [here](https://github.com/grundic/awesome-python-models?tab=readme-ov-file#odm-orm-active-record) and [here](https://github.com/vajol/python-data-engineering-resources/blob/main/resources/orms-for-python.md#list-of-orms)


### Utilities

> These are great for quickly working with your data

- [JQ](https://jqlang.org/) (for [manipulating `json`](https://programminghistorian.org/en/lessons/json-and-jq), and it's [playground](https://play.jqlang.org/) with some [examples](https://programminghistorian.org/en/lessons/json-and-jq))
- [SQLite Utils](https://sqlite-utils.datasette.io/en/stable/) (rapid manipulation and CLI)
- [VS Code](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) plugin

### Scaling

> SQLite is growing in popularity for production servers

- [Litestream](https://litestream.io/) for backups (costs pennies per day)
- [Litefs](https://github.com/superfly/litefs) for clusters and [local-first](https://fly.io/docs/litefs/) (like [Turso](https://turso.tech/))


## Books

1. [SQLite books](https://www.sqlite.org/books.html)

## Courses

> Google "udemy/coursera sql course"

I think the original SQL courses I did ages back are on Udemy.

- [Database design](https://www.youtube.com/playlist?list=PL_c9BZzLwBRK0Pc28IdvPQizD2mJlgoID) in 8 hours


## ⚠️ Warnings

### Security

1. [Writing raw SQL](https://www.youtube.com/watch?v=Cp3bXHYp-bY) (things to watch out for)
2. [About ORMS](https://www.fullstackpython.com/object-relational-mappers-orms.html) (safer than raw SQL)

### SQLite
#### Types

> Sqlite is very permissive.
> It isn't at all Type safe!

SQLite datatypes are [very simple](https://www.sqlite.org/datatype3.html), with main ones being `NULL`, `INTEGER`, `TEXT` (and occasionally `BLOB`). You can enable [strict tables](https://www.sqlite.org/stricttables.html) (or [strict mode](https://sqlite.org/src/wiki?name=StrictMode)), but some ORMs use custom types so these will restrict you somewhat. By default SQLite will guarantee `NOT NULL` and `UNIQUE` values, but you've got to take care not to introduce bugs when `INSERT`ing row values. Postgres is far more strict. An example below:

```sql
-- Creates `null` column name (missing name) 
ALTER TABLE BandMember ADD COLUMN TEXT;
-- Not strict by default! 🤦
-- Ignores types and bounds; infers types if incorrect.
CREATE TABLE shit_types (a INT, b VARCHAR(10));
INSERT INTO shit_types (a,b) VALUES('123',1234567891011);
-- 123|1234567891011
```

#### Pragmas

> You **must** notify SQLite to respect foreign keys for **every** connection!
> This will make sure that `DELETE` [cascades](https://www.techonthenet.com/sqlite/foreign_keys/foreign_delete.php) (if foreign key deleted)

```sql
-- For every connection, set this ...
-- Especially for `INSERT` and `DELETE`
PRAGMA foreign_keys=on;
```


