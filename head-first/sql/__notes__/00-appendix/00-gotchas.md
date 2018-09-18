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


### Escaping strings

```sql
INSERT INTO easy_drinks
VALUES ('Rob''s soda');
```

- Postgres prefers [an extra single quote](https://bit.ly/2xqzvKI) (there's other ways too)
- Where possible, let your programming language [do it for you](https://stackoverflow.com/a/12317363)!
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
