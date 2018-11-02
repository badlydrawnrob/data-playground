## Gotchas

![](./img/gotchas.jpg)

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


### You don't need a comma for that!

```sql
SELECT col_name FROM table
WHERE col_name > 't'  -- No need for a comma here
  AND price < 4;      -- but make sure you end with a semi-colon;
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
- Always try to delete unused columns or data
- Always add sensible limits to data types


### Aggregate functions

- Postgres expects columns in `GROUP BY` when using aggregate functions
