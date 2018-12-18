## VIEW

> `VIEW` simplifies your queries, making them easier to remember

If you find yourself entering the same queries, over and over, it can become tedious. There's a solution for that!

1. Store your query for reuse
2. Simplify and easy to remember
3. Hide sensitive data
4. Avoid making mistakes

```SQL
-- Store view
CREATE VIEW web_designers AS
SELECT mc.first_name, mc.last_name, mc.phone, mc.email
FROM my_contacts mc
NATURAL JOIN job_desired jd  -- or, INNER JOIN
WHERE jd.title = 'Web Designer';
-- Use view
SELECT * FROM web_designers
```

The view actually behaves similar to a _subquery_:

```SQL
SELECT * FROM (
  SELECT ...
  FROM ...
  NATURAL JOIN ...
  WHERE jd.title = 'Web Designer'
) AS web_designers;
```

- You must alias the `SELECT`
- So the `FROM` recognises it as a table

### Updating the view

You can change the underlying structure of the `VIEW`, or table, without the user (or app) needing to know about it. `DROP VIEW` to delete it (do this before deleting it's table).

### Views and security

- A view can technically use `UPDATE`, `INSERT`, `DELETE` (using `CHECK OPTION`)
- But it's best to use a `VIEW` as **read only**
- **Be careful** when giving others access to views!!
