## Normalisation

Normalisation simply means working with standard rules, making it easier for you and your team to work on together.

- It makes our database easier to search
- It makes our database smaller
- It makes our queries faster!


### 1NF

1. Each row of data must contain atomic values
2. Each row of data must be unique

### You need a primary key

To make avoid duplicate rows you'll need a unique identifier, or **primary key**.

1. A primary key _must_ be unique (to it's column)
2. A primary key can't be `NULL`
3. When you `INSERT` a record, the primary key _must_ be given
4. A primary key can't be changed once set
