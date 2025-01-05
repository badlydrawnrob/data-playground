## Merging data

There are **3 ways** to merge all our `interest` tables! It can be helpful to know different ways to perform a task, as it can speed up your queries. Let's use our `professions` table as an example.

### `CREATE TABLE`, then `INSERT` with `SELECT`

1. The `SELECT` holds our list of values
    + You'd usually use `VALUES` here
2. `GROUP BY` helps us avoid duplicates
3. Add our values alphabetically

```sql
CREATE TABLE profession (
  id SERIAL,
  profession varchar(20)
);

INSERT INTO profession (profession)
  SELECT profession     -- #1
  FROM my_contacts
  GROUP BY profession   -- #2
  ORDER BY profession;  -- #3
```


### `CREATE TABLE` with `SELECT`, then `ALTER` to add primary key

1. Grab our values from `my_contacts` `profession` column
    + Which populates our new `profession` table
2. Add in our primary key after

```SQL
CREATE TABLE profession AS
  SELECT profession     -- #1
  FROM my_contacts
  GROUP BY profession
  ORDER BY profession;

ALTER TABLE profession
ADD COLUMN id SERIAL;   -- #2
```


### `CREATE`, `SELECT` and `INSERT` — all at the same time!

1. Create the table (as you would normally)
2. Add on the `SELECT` statement holding all our `profession` values

```sql
CREATE TABLE profession (
  id SERIAL,
  profession varchar(20)
) AS
  SELECT profession
  FROM my_contacts
  GROUP BY profession
  ORDER BY profession;
```
