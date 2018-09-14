## SELECT statement

```sql
SELECT * FROM my_contacts;  -- * is a wildcard for "all columns"
```

Displays all records from the table `my_contacts`.


### Limit the results

```sql
SELECT first_name, location FROM my_contacts;
```

Returns only the columns you'd like to view — it also _speeds up_ the query!
