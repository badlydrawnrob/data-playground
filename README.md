# README

> A soft play area for data!

## Goals

> 1. Very light data analysis
> 2. Very small app prototyping
> 3. Storing Marketing/Ads data

Examples such as the **Programming Flashcards App**, **Google Ads**, **Simple Analytics** research, **Library Data**, and so on. Should involve basically ZERO database admin, unless absolutely necessary.


## Notes

> - [Appropriate uses for SQLite](https://www.sqlite.org/whentouse.html)
> - When to use [Postgres -vs- SQLite](https://www.boltic.io/blog/postgresql-vs-sqlite)
> - [Modern SQL](https://modern-sql.com/) and what's changed

### Some handy settings

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

- [Enso](https://help.enso.org/) (data prep and visualisation)
- [SQLite Utils](https://sqlite-utils.datasette.io/en/stable/) (rapid manipulation and CLI)
- [JQ](https://jqlang.org/) (for manipulating `json`, and it's [playground](https://play.jqlang.org/))
- [SQL for Humans](https://github.com/kennethreitz/records) (records tool)
    - May be better used for internal use than app use (security)
- [VS Code](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) plugin
- [Mockaroo](https://www.mockaroo.com/) (generate mock data)
- [Convert files to SQL](https://sqlizer.io/) (eg: `.csv` -> `.sqlite`)
- [5 best GUIs](https://turso.tech/blog/5-best-free-sqlite-gui) for SQLite
- ORM [lists](https://github.com/grundic/awesome-python-models?tab=readme-ov-file#odm-orm-active-record) and [other lists](https://github.com/vajol/python-data-engineering-resources/blob/main/resources/orms-for-python.md#list-of-orms) and [Piccalo](https://piccolo-orm.com/)


## Books

1. [SQLite books](https://www.sqlite.org/books.html)

## Courses

> Google "udemy/coursera sql course"

I think the original SQL courses I did ages back are on Udemy.


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


