## EXISTS

```sql
SELECT mc.first_name firstname, mc.last_name lastname, mc.email email
FROM my_contacts AS mc
WHERE EXISTS (
  SELECT * FROM contact_interest AS ci
  WHERE mc.contact_id = ci.contact_id
);
```

Find data from `my_contacts` where `contact_id` shows up at least once in `contact_interest` table.

### NOT EXISTS

```sql
SELECT mc.first_name firstname, mc.last_name lastname, mc.email email
FROM my_contacts mc
WHERE NOT EXISTS (
  SELECT * FROM job_current jc
  WHERE mc.contact_id = jc.contact_id
);
```

Find all the rows in the outer query, for which no rows exist in a related table.
