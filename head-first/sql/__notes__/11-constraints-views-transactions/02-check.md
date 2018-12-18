## CHECK

![Image of scheme]()

A `CHECK` is a [constraint](https://www.postgresql.org/docs/current/ddl-constraints.html) that restricts and validates input. You've already seen a few of these already:

- `NOT NULL`
- `PRIMARY KEY`
- `FOREIGN KEY`
- `SERIAL` (or `UNIQUE`)

Imagine our database table `my_contacts`. Our new recruit, Jim, has the task of adding new entries:

1. He's adding in a new member, _Pat_
2. He isn't sure if Pat is a `M`ale or `F`emale
3. To avoid a `NULL` entry, he uses `'X'` instead


```SQL
-- Jim looks up the profession id
SELECT profession_id WHERE profession = 'teacher';
-- He also looks up status id
SELECT status_id WHERE status = 'single';
-- Finally, he adds Pat to the database
-- including gender, profession_id, status_id
INSERT INTO my_contacts
VALUES ('Pat', 'patmurphy@someemail.com', 'X', 19, 3)
```

What happens if, in the future, we count `M`ale or `F`emale members? We'd have some members with gender `X`, so our results are messed up:

```sql
-- All members (1000)
SELECT * FROM my_contacts;
-- Males (450)
SELECT * FROM my_contacts
WHERE gender = 'M';
-- Females (300)
SELECT * FROM my_contacts
WHERE gender = 'F';
```      


### Check constraint to the rescue!

```SQL
CREATE TABLE piggy_bank (
  id INT SERIAL PRIMARY KEY,
  coin CHAR(1) CHECK (coin IN ('P', 'N', 'D', 'Q'))
);
```
```text
[data] ----> check ----> success/error
```

Say if we had a piggy bank, which could only take a certain type of coin. We can check it against a list of values, as above:

1. Similar to `WHERE` clause
2. You can use `AND`, `OR`, `IN`, `NOT`, `BETWEEN`
3. You can also use things like string functions

So, we can now update our original `gregs_list` table to avoid Jim making his `X` errors:

```sql
UPDATE TABLE my_contacts
ADD CONSTRAINT constraint_name CHECK (gender IN ('M', 'F'));
```


### Notes on MySQL

MySQL **does not** enforce data integrity with `CHECK` (there are alternative methods).
