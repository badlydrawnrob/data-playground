## WHERE statement

Say we'd like to display someone specific, we need to list all the `Anne`s from our contacts table. We could search through the entire table, but it's easier to narrow our search:

```sql
SELECT * FROM my_contacts
WHERE first_name = 'Anne';  -- first_name is Anne
```

- If any rows match contain `'Anne'` in `first_name`, it returns all data for that row
- If there's no match, the row isn't returned


### Comparison operators

- `<` less than
- `>` greater than
- `<=` less than or equal to
- `>=` greater than or equal to
- `=` equal
- `<>` or `!=` not equal


### Other expressions

```sql
-- More than one expression
expression AND expression
expression OR expression

-- Includes endpoint values in the range
a BETWEEN x AND y      -- same as `a >= x AND a <= y`
a NOT BETWEEN x AND y  -- same as `a < x OR a > y`

-- NULL is not equal to anything
expression IS NULL
expression IS NOT NULL
```
