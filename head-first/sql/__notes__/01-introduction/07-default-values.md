## Default values

The default value is `NULL`. If you create a record with empty column values, that's what you'll get. You can think of it as being an _undefined_ entry.

```sql
CREATE TABLE no_empty_spaces (
  spade VARCHAR(10),           -- can be left blank
  bucket VARCHAR(10) NOT NULL  -- a bucket always has to be full!
)
```

Some columns should _always_ have values. To do this, you use `NOT NULL`, which forces you to fill the column for a record.

### Which should I use?

> If the data is clean and complete it's easier for you to analyse later.

1. Will you need to search a row by this field?
    - Use `NOT NULL`
2. Or will the data need to be filled in later?
    - Use `NULL`
3. How important is it that the data is there?


### People are lazy ...

We can make it easier for people to fill in an entry, by including a `DEFAULT` value:

- If the value is usually this one, set it as a default
- The default must be the same type as the column
- If it's important to get the value right, use `NULL` or `NOT NULL`

```sql
CREATE TABLE doughnut_list (
  doughnut_name VARCHAR(10) NOT NULL,
  doughnut_type VARCHAR(8) NOT NULL,
  doughnut_cost DECIMAL(3,2) NOT NULL DEFAULT 1.00  -- Total 3 digits: 1 full, 2 decimal
)
```

The results would look something like this:

```bash
doughnut_name | doughnut_type | doughnut_cost
---------------+---------------+---------------
krispy        | jammy         |          2.00
dunkin        | iced          |          1.00
robs          | dusted        |          1.00
```
