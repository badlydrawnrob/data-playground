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


## ⚠️ Warnings

### SQLite

> Sqlite is very permissive.
> It isn't at all Type safe!

You can, however, enable [strict mode](https://sqlite.org/src/wiki?name=StrictMode) or [strict tables](https://www.sqlite.org/stricttables.html). Be careful with bugs when dealing with SQLite, as it's not as strict as Postgres. For example, if you write improper SQL such as:

```sql
-- Creates `null` column name (missing name) 
ALTER TABLE BandMember ADD COLUMN TEXT;
-- These types are allowed 🤦
CREATE TABLE shit_types (a INT, b VARCHAR(10));
INSERT INTO shit_types (a,b) VALUES('123',1234567891011);
-- 123|1234567891011
```

#### Foreign keys are not respected (fix)

> You **must** notify SQLite to respect foreign keys for **every** connection!

```sql
-- For every connection, set this ...
-- Especially for `INSERT` and `DELETE`
PRAGMA foreign_keys=on;
```


## Other courses

> Google "udemy/coursera sql course"

I think the original SQL courses I did ages back are on Udemy.
