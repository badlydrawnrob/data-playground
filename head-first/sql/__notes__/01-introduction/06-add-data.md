## Adding data to a table

> Insert your name right here!

```sql
INSERT INTO table_name (column_name, column_name, ...)
VALUES ('value', 'value', ...);
```

1. `'Value'` must be in the same order as their `column_name`
2. `'single quotes'` for all text and character types
3. No comma after last `column_name`
4. No comma after last `value`
5. You can leave out `(column_name, ...)`, but values should match your table structure _exactly_ 
