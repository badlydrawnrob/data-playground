## BETWEEN statement

```sql
-- Order matters!
value BETWEEN low AND high      -- same as `a >= x AND a <= y`
value NOT BETWEEN low AND high  -- same as `a < x OR a > y`
```

Example with numbers:

```sql
-- Includes endpoint values in the range
WHERE count BETWEEN 10 AND 30;  -- 10—30
```

Example with characters:

```sql
-- Does not include endpoint values in the range
WHERE string BETWEEN 'r' and 'm';  -- 'r' to 'l'
```
