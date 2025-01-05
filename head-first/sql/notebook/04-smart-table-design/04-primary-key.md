## You're going to need a primary key

![Just like Harry Potter, you need to find the primary key!](./img/primary-key.jpg)

To make avoid duplicate rows you'll need a unique identifier, or **primary key**.

1. A primary key _must_ be unique (to it's column)
2. A primary key can't be `NULL`
3. When you `INSERT` a record, the primary key _must_ be given
4. A primary key can't be changed once set

### There's 3 ways to find a primary key

1. Use an existing column in your table that _you're sure_ is always unique
2. Create a new column and _manually_ set a number for each row
3. Create a new column and _automatically_ increment a number for each row

For most cases, you'll want to generate a new column with a unique _automatically_ incrementing ID.
