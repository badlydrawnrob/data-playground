## NOT statement

You can return values that are `NOT` the same as your statement. Combine it with `WHERE` to make the magic happen! There's two ways to write it:

1. `WHERE NOT [expression] [value]`
2. `WHERE [expression] NOT [value]`

```sql
SELECT * FROM drinks
WHERE NOT price > 6;
-- is the same as
SELECT * FROM drinks
WHERE price NOT > 6;
```

Here's some other examples:

```sql
-- Range
WHERE price NOT IN (5, 6, 8);
-- Not empty
WHERE price IS NOT NULL;
-- Multiple expressions
WHERE price NOT > 6
  AND name LIKE 'fiz%';
```

**Be careful:** It's often easier to use standard expressions rather than `NOT`!
