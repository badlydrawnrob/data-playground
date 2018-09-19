## Adding data to a table

![Insert your `('value')` into the table!](./img/insert-into-table.jpg)


```sql
INSERT INTO table_name (column_name, column_name, ...)
VALUES ('value', 'value', ...);
```

1. `'Value'` must be in the same order as their `column_name`
2. `'single quotes'` for all text and character types
3. No comma after last `column_name`
4. No comma after last `value`

You can leave out `(column_name, ...)`, but values should _exactly_ match your table structure:

```sql
INSERT INTO table_name
VALUES ('value_of_col_1', 'value_of_col_2', ...);
```

Or, you can leave out some column `'values'`, but you _must_ specify the `column_name`s you _are_ including


### Insert multiple records (or rows)

```sql
INSERT INTO table_name (column_name, column_name, ...)
VALUES ('value', 'value', ...),  -- Separate with a comma
       ('value', 'value', ...);  -- Value lists must all be the same length
```

Simply add more rows in the `VALUES` statement, separated with a comma `,`.
