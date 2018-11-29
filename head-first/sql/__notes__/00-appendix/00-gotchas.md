## Gotchas

![](./img/gotchas.jpg)

**These notes and this text are true of [Postgres 11](https://www.postgresql.org/docs/11/)** — they're subject to change, so do your homework!


### SELECT queries

These don't seem like they should work, but they do. These queries **are not correct**, just a little forgiving:

```sql
SELECT * FROM easy_drinks WHERE amount2 = 6;      -- Matches 6.0
SELECT * FROM easy_drinks WHERE main > 'soda';    -- Weirdly, yes
SELECT * FROM easy_drinks WHERE amount1 = '1.5';  -- Treats as a number
```

### Datatype queries

| Type                    | Single quotes | No quotes |
| ----------------------- | ------------- | --------- |
| `char`                  | ✔             |           |
| `varchar`               | ✔             |           |
| `text`                  | ✔             |           |
| `date`                  | ✔             |           |
| `datetime`, `timestamp` | ✔             |           |
| `int`                   |               | ✔         |
| `decimal`               |               | ✔         |


### Escaping characters

```sql
-- Escape strings
INSERT INTO easy_drinks
VALUES ('Rob''s soda');
-- Escape columns
SELECT "name", price FROM easy_drinks;
```

- Postgres prefers [an extra single quote](https://bit.ly/2xqzvKI)
    + You can also [escape with a backslash](https://bit.ly/2Rl4znu)
- Where possible, let your programming language [do it for you](https://stackoverflow.com/a/12317363)!
    + [Use a GUI](https://postgresapp.com/documentation/gui-tools.html) for working with raw SQL
- In standard sql, you can escape with a backslash `\'`
- Never use double quotes to escape, as it can cause your software problems
- Use the same method when using a `SELECT` query


### You DON'T need a comma for that!

```sql
SELECT col_name FROM table
WHERE col_name > 't'  -- No need for a comma here
  AND price < 4;      -- but make sure you end with a semi-colon;
```


### You DO need a comma for that!

```sql
ALTER TABLE my_table
ADD COLUMN column_name int,  -- watch out for those commas!
ADD COLUMN column_name int
```


### Any value is better than NULL

- It's best to add something, rather than leaving values `NULL`
- It can't be directly selected from a table
- Sometimes it may even be best to delete (or ignore) them completely!


### Deleting records

- Always include a `WHERE` statement, or you'll delete _all_ your rows!
- Always check your `WHERE` statement for errors
- Always check your `DELETE` order
- Always check other rows for _shared values_ (that you don't want to change)
- If in doubt: **use `SELECT` first to check your `WHERE` statement!**


### Updating records

- Always include a `WHERE` statement, or you'll update _all_ your rows!
- Always check your `WHERE` statement for errors
- Always check other rows for _shared values_ (that you don't want to change)
- Order matters: (highest first: `{1.50 -> 2.00, 1.00 -> 1.50}`)
    + Two statements may update the same column
    + Be specific with your `WHERE` clauses :)
- Be sure to check your new values — are they _all_ what you expected?
- If in doubt: **use `SELECT` first to check your `WHERE` statement!**


### Speed, size, accuracy

- Always make your data as simple as possible
    + Reduce cognitive load (and potential mistakes)
    + Make it fast and easy to: enter, monitor, edit
    + See [Atomic Data](#atomic-data) chapter notes
- Always try to delete unused columns or data
- Always add sensible limits to data types
- Always request what you _need_ (`limit` results)
    + But _you must_ make sure the order is predictable (`order by`)
    + Row order _is not guaranteed_ in SQL queries
- Always keep a diagram of your schema
    + Keep data and schema independent of each other


### Aggregate functions

- Postgres expects columns in `GROUP BY` when using aggregate functions
- It's generally good practice to ignore `0` and `NULL` values:
    + `WHERE column_name > 0` or `WHERE column_name IS NULL`
- `NULL` is **never returned** by any aggregate function
    + `NULL` is not the same as zero!
- Use `GROUP BY` when you want to use aggregate functions
- Use `SELECT DISTINCT` when you want to remove duplicates
    + It's better to use an [inner select](https://stackoverflow.com/a/14732410)
    + Especially when using `count()` or another aggregate function!
    + Returns the same values as `GROUP BY` (without aggregate functions)
