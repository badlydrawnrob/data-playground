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


### Matching strings

You can also use comparisons for characters:

```sql
SELECT * FROM my_contacts
WHERE first_name > 'A';  -- Returns values beginning with `B`—`Z`

SELECT * FROM my_contacts
WHERE first_name >= 'C';  -- Returns values (including `C`), so `C`—`Z`
```
