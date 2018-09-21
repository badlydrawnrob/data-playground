## Moving location

![](./img/moving-location.jpg)

To finish off our new location we need to:

1. Combine our string Functions
2. Create two new columns, `city` and `state`
3. Use our old `location` value to `SET` our new columns
4. Delete our old `location` column

```sql
ALTER TABLE my_contacts
ADD COLUMN city varchar(30),
ADD COLUMN state char(2);
-- This will set ALL rows with new values
UPDATE my_contacts
SET city = split_part(location, ',', 1);
UPDATE my_contacts
SET state = right(location, 2);
-- Delete our old column
ALTER TABLE my_contacts
DROP COLUMN location;
```
