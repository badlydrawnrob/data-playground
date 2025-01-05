## NULL values

You cannot select a `NULL` value directly

```sql
-- This WILL work ...
SELECT doughnut FROM doughnut_list
WHERE doughnut IS NULL;
-- but this WILL NOT work
SELECT doughnut FROM doughnut_list
WHERE doughnut = NULL;  -- NULL is not equal to anything
```

However, if you use `WHERE` on non-empty values, a `NULL` value will show:

```sql
SELECT type_of_doughnut FROM doughnut_ratings
WHERE location = 'Krispy King' OR rating > 5;
```
```text
type     
--------------
plain glazed
plain glazed
plain glazed

jelly
(5 rows)
```

### Other options

You can display values that _are_ NULL or only values that _are not_ NULL.

```sql
-- NULL is not equal to anything
expression IS NULL
expression IS NOT NULL
```
