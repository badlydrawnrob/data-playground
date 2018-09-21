## Styleguide

Some useful tips:

1. [SQL Style Guide](https://www.sqlstyle.guide)


### General guidelines

```sql
-- UPPERCASE sql statements
-- Always ends in semi-colon
CREATE DATABASE db_name;

-- lowercase, snake_case
CREATE TABLE db_table (
  column_name varchar(10),  -- use correct data type
  ...
);

-- Always use single quotes
-- Numbers do not need quotes
INSERT INTO db_table (column_name, column_name)
VALUES ('value', 1.0),  -- use commas
       ('value', 2.0);  -- except the last one!
```
