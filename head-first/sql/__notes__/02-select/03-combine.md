## Combining your queries

```sql
SELECT email FROM my_contacts
WHERE profession = 'Computer programmer';
```

The `SELECT` columns are the ones displayed — you can use whatever columns you like in the `WHERE` query to refine your results: mix and match!

```sql
SELECT first_name, email FROM my_contacts
WHERE location = 'San Fran, CA'
  AND gender = 'F'
  AND first_name = 'Anne';
```

You can mix character and numeric values too ...

```sql
SELECT easy_drinks FROM drinks
WHERE main = 'soda'
  AND amount1 > 1;
```


### Other expressions

```sql
-- More than one expression
expression AND expression
expression OR expression
```
