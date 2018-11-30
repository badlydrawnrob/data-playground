## Natural join

Natural joins only work if the column you're joining by has _the same name on both tables_. It'll _naturally_ attempt to join the two tables on their _identical_ column names.

```sql
SELECT boys.boy, toys.toy
FROM boys
  NATURAL JOIN
  toys;
```

Will return the very same result from our first [inner join](#innerjoin)
