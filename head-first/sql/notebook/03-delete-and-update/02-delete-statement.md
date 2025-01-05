## DELETE statement

You can use a `DELETE` statement to remove a single, or multiple rows.

- Use it in combination with `WHERE`
- It's similar to your `SELECT` statements!

```sql
-- Delete all Zippo's rows
DELETE FROM clowns_info
WHERE first_name = 'Zippo';
-- Delete only the one we want
DELETE FROM clown_info
WHERE first_name = 'Zippo'
  AND activities = 'dancing, singing';
```

**Important:** Make sure you always include a `WHERE` statement, or you'll delete _all_ your rows!
