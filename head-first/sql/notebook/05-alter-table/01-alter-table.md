## ALTER TABLE statement

![You can alter your table anyway you like! ](./img/chalkboard-table.jpg)

You've already used the `ALTER TABLE` statement, but there's lots more it can do!!

```sql
ALTER TABLE table_name
-- Add a statement below to make the magic happen!
```

### It goes great with ...

Use it with the following statements. You can [combine statements together](https://stackoverflow.com/questions/25398603/postgresql-query-to-rename-and-change-column-type-with-single-query#25398701), too:

| Statement                                    | Does this                              |
| -------------------------------------------- | -------------------------------------- |
| `ADD [ COLUMN ] col_name [type]`             | Adds a new column                      |
| `DROP [ COLUMN ] col_name`                   | Deletes a column (and _all_ it's data) |
| `ALTER [ COLUMN ] col_name [type]`           | Change a column type                   |
| `RENAME [ COLUMN ] col_name TO new_col_name` | Rename a _column_ ([no multiple columns](https://stackoverflow.com/questions/23274679/renaming-multiple-columns-in-one-statement-with-postgresql/23274931#23274931)) |
| `RENAME table_name TO new_table_name`        | Rename a _table_                       |


### Tidy up names

```text
----[ projekts ]----------------

     Column       |         Type          |       
------------------+-----------------------+
number            | integer               |
descriptionofproj | character varying(50) |
contractoronjob   | character varying(10) |
```

Let's take the following database as an example. There's lots that could be improved:

```sql
-- First, let's give the table a better name
ALTER TABLE projekts
RENAME TO project_list;
-- We can rename the columns too!
-- #1: Escape a keyword
ALTER TABLE project_list
RENAME COLUMN "number" TO proj_id;  -- #1
ALTER TABLE project_list
RENAME COLUMN descriptionofproj TO proj_desc;
ALTER TABLE project_list
RENAME COLUMN contractoronjob TO con_name;
-- We need more data! Let's add some columns
-- #2: Multiple statements allowed
-- #3: This is the same as `decimal(7, 2)`
ALTER TABLE project_list
ADD COLUMN con_phone varchar(11), -- #2
ADD COLUMN start_date date,
ADD COLUMN est_cost numeric;  -- #3
```

### Changing data types

Before changing your data type, **watch out**!

- If your new data type _isn't_ compatible, you'll get an error
- If your new data type _is_ compatible and too long, it gets truncated (`'Bobby' -> 'B'`)

```sql
ALTER TABLE project_list
ALTER COLUMN proj_desc TYPE varchar(120);  -- Add more space
```

### Adding a primary key

#### The wrong way

You'd think this would work ...

```sql
-- Use `proj_id` (number) as auto-increment primary key
-- #1: Change type to serial
-- #2: Add the primary key
ALTER TABLE project_list
ALTER COLUMN proj_id TYPE SERIAL,
ALTER COLUMN proj_desc TYPE varchar(120),
ADD PRIMARY KEY (proj_id);
```

#### The right way

But [it doesn't seem to](https://stackoverflow.com/questions/16474720/alter-data-type-of-a-column-to-serial#16474780). It's much easier to:

```sql
-- 1: Create `proj_id_new` column
-- 2: Make it a `serial` type
-- 3: And make it the primary key
ALTER TABLE project_list
ADD COLUMN proj_id_new serial PRIMARY KEY;
```


### Removing a column

We no longer need the `start_date` and `proj_id` .. let's drop those suckers!

```sql
ALTER TABLE project_list
DROP COLUMN start_date,
DROP COLUMN proj_id;
-- Let's rename our new primary key too ..
ALTER TABLE project_list
RENAME proj_id_new TO proj_id;
```


### Now our table is fully pimped!

```text
 Column   |         Type          | Collation | Nullable |                      Default                      
----------+-----------------------+-----------+----------+---------------------------------------------------
proj_desc | character varying(50) |           |          | NULL::character varying
con_name  | character varying(10) |           |          | NULL::character varying
con_phone | character varying(11) |           |          |
est_cost  | numeric               |           |          |
proj_id   | integer               |           | not null | nextval('project_list_proj_id_new_seq'::regclass)
```

Unfortunately, we can't do much about the order as Postgres won't let us do that easily (at the time of writing). It's possible, but fiddly and a bit risky.
