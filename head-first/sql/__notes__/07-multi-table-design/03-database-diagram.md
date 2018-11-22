## Database diagram

![](./img/database-diagram.jpg)

You can view your database as objects (tables), and lists (columns)

1. Select the non-atomic data you'd like to split out
2. Create a new object (table)
3. Create attributes for the table (columns)
4. Make sure you add an `id` field for your attribute rows

Let's take `gregs_list` as an example. Once we've created our new table, we need to find a way to link the interests to the person.

- It's generally best to use the **id** (in this case, _primary key_)
- This will link our `interests` table with a person's `contact_id`
- The column you link to should be **unique**
- This unique link is called a **foreign key**

A _foreign key_ is a column that links a _primary key_ of another table. This primary key is now the _parent key_ of the `interests` table. The `my_contacts` table is the _parent table_.


### Constraint

![You're going to need to constrain your child!](./img/parent-child.jpg)

A constraint **only** allows you to add values that exist in the parent table. It's also called _referential integrity_, which helps you avoid breaking your table, avoids "dead" data, keeping your database speedy.

- The value you add into your _foreign key_ must already exist in your _primary key_


### Create our table with a foreign key

```SQL
CREATE TABLE interests (
  int_id SERIAL PRIMARY KEY,
  interest varchar(50) NOT NULL,
  contact_id int NOT NULL              -- #1
  REFERENCES my_contacts (contact_id)  -- #2
);
```

1. Create a field for our foreign key
2. Link it to our primary key table
    + `(contact_id)` is optional

The [`FOREIGN KEY`](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-FK) statement is only needed in Postgres when creating a foreign key with more than one column.

### Deleting a row

If you try to delete a foreign key row, within a parent table, you're going to have problems my friend.

- You _must_ delete it's linked child table rows first.
