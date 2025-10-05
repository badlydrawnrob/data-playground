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

```terminal
-- Launch sqlite
sqlite3 database.sqlite

-- Quit sqlite
.quit
```

### Handy settings

> You can [save settings](https://stackoverflow.com/a/42910299) in your `~/` home directory with an `.sqliterc` file!

```sql
-- Show table headings and column format
.headers on
.mode column

-- Show pretty printed schema
.schema --indent
```


## Tools

> True as of 2025

### GUIs

- [5 best GUIs](https://turso.tech/blog/5-best-free-sqlite-gui) for SQLite (and [Tad](https://www.tadviewer.com/) for pivots)
- [Enso](https://help.enso.org/) (data prep and visualisation)
- [Mockaroo](https://www.mockaroo.com/) (generate mock data)

### Code

> There are LOTS of frameworks for dealing with data.
> I may consider [Ocaml](https://aantron.github.io/dream/)/[Elixir](https://www.phoenixframework.org/)/Go/Gleam/Roc or [another language](https://survey.stackoverflow.co/2024/technology) later ... for now, Python!

- [JQ](https://jqlang.org/) (for [manipulating `json`](https://programminghistorian.org/en/lessons/json-and-jq), and it's [playground](https://play.jqlang.org/) with some [examples](https://programminghistorian.org/en/lessons/json-and-jq))
- [VS Code](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) plugin
- Python list of [ORMs](https://github.com/grundic/awesome-python-models?tab=readme-ov-file#odm-orm-active-record) and [here](https://github.com/vajol/python-data-engineering-resources/blob/main/resources/orms-for-python.md#list-of-orms) and [ice axe](https://github.com/piercefreeman/iceaxe)
- [Piccalo](https://piccolo-orm.com/) (ORM for FastApi with [notes](https://github.com/piccolo-orm/piccolo/issues/1187) for pragma/types)
- Alternatively, [Sanic](https://sanic.readthedocs.io/en/stable/) and [Peewee ORM](https://docs.peewee-orm.com/en/latest/peewee/database.html#sanic) (or non-async API)
- [SQL for humans](https://github.com/kennethreitz/records) (Just write SQL in Python!)
    - Great for internal admin (where security isn't a concern)
- [SQLite Utils](https://sqlite-utils.datasette.io/en/stable/) (rapid manipulation and CLI)


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

You can, however, enable [strict tables](https://www.sqlite.org/stricttables.html) (or [strict mode](https://sqlite.org/src/wiki?name=StrictMode)). Be careful with bugs when dealing with SQLite, as it's not as strict as Postgres. For example, if you write improper SQL such as:

```sql
-- Creates `null` column name (missing name) 
ALTER TABLE BandMember ADD COLUMN TEXT;
-- These types are allowed 🤦
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


