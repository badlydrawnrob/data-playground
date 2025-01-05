## Deleting a table

![You need to drop that sucker!](./img/mic-drop.jpg)

You can't recreate an existing table or database:

```psql
database_name=> CREATE TABLE my_contacts ( ... );
ERROR:  relation "my_contacts" already exists
```

Instead, you'll need to `DROP` the table:

```sql
DROP TABLE my_contacts;
```

And recreate it with the `CREATE TABLE` sql command
