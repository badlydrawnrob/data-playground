## Combining your queries

```sql
SELECT email FROM my_contacts;
WHERE profession = 'Computer programmer';
```

You can mix and match the column names with the `WHERE` query ...

```sql
SELECT first_name, email FROM my_contacts
WHERE location = 'San Fran, CA'
  AND gender = 'F'
  AND first_name = 'Anne';
```

Or both character and numeric values

```sql
SELECT easy_drinks FROM drinks
WHERE main = 'soda'
  AND amount1 > 1;
```
