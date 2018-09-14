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
VALUES ('Rob\'s soda');
```

- Never use double quotes to escape, as it can cause your software problems
- Use the same method when using a `SELECT` query
