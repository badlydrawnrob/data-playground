## Correlation

### Non-correlated subquery

```SQL
-- examples of non-correlated subquery
SELECT mc.first_name, jc.salary
FROM my_contacts AS mc
NATURAL JOIN job_current AS jc
WHERE jc.salary > (
  SELECT jc.salary
  FROM my_contacts mc
  NATURAL JOIN job_current jc
  WHERE email = 'andy@weatherorama.com'
);
```

An inner query that **is not** referenced in the outer query.

- `Y` doesn't know about outer query `X` (it's a single value)
- But `X` is dependant on the result of `Y`

Here, the inner query is processed first.


### Correlated subquery

```SQL
-- example of subquery in a select column
-- returns those who have 3 interests
SELECT mc.first_name, mc.last_name
FROM my_contacts AS mc
WHERE 3 = (
  SELECT COUNT(*) FROM contact_interest
  WHERE contact_id = mc.contact_id
);
```

A correlated subquery **does** reference the outer query.

- `Y` is dependant on the outer query `X`
    - i.e: reference an alias within subquery
