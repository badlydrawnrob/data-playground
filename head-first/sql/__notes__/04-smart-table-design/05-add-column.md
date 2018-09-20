## Adding a primary key column

### Method 1: From scratch (or recreate table)

1. Export your data
2. Create a new table (with a primary key column)
3. Import the old data into the new table

```sql
CREATE TABLE table_name (
  id SERIAL PRIMARY KEY
  ...
);

-- Leave out the `id` column: it automatically populates
INSERT INTO table_name (...)
VALUES (...)
```

### Method 2: UPDATE TABLE statement

```sql
-- Add a primary key column
ALTER TABLE table_name
ADD COLUMN id SERIAL PRIMARY KEY;

-- Or, alter an existing column
ALTER TABLE table_name
ADD PRIMARY KEY (column_name);
```


### Postgres primary key notes:

- [`serial`](http://www.postgresqltutorial.com/postgresql-serial/) is the [equivalent of `auto_increment`](https://stackoverflow.com/questions/787722/postgresql-autoincrement) ...
- but there are [other types](https://stackoverflow.com/questions/11778102/what-is-the-right-data-type-for-unique-key-in-postgresql-db) and [methods](http://www.postgresqltutorial.com/postgresql-primary-key/) you [can use](https://www.starkandwayne.com/blog/uuid-primary-keys-in-postgresql/) too ...
- currently there's [no way to alter column order](http://wiki.postgresql.org/wiki/Alter_column_position) with Postgres.
