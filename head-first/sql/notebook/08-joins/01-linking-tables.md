## Linking tables

![](./img/set-theory.png)

Now we've created our _database schema_, we'll need a way to view our data together. **Joins** help us link multiple tables together ...

### Let's organise our contacts first

You learned how to organise _greg's list_ in the previous chapter, to a better 3NF schema. How would we go about doing this in code? Let's take the `interests` column as an example:


```text
interests                              id | interests
-----------------------------    ==>   ---+----------
kayaking, reptiles, cooking            1  | kayaking
                                       2  | reptiles
                                       3  | cooking
```

1. Find all _unique_ values in the original `interests` table rows
2. Create a new `interests` table
3. Copy values to new table (no duplicates!)
4. Delete the original `interests` column

For every non-atomic column we need to extract into it's own table, we follow these steps.


#### How to do it?

Remember our [girl guides](#aggregatefunctions)? We used `SELECT DISTINCT` to retrieve the dates, without duplicates. Let's do the same to see if we can pull out unique values:

```sql
SELECT DISTINCT interests
FROM my_contacts;
```
```text
-[ RECORD 1 ]-----------------------------
interests | RPG, kayaking
-[ RECORD 2 ]-----------------------------
interests | RPG, anime
...
-[ RECORD 10 ]----------------------------
interests | women
-[ RECORD 11 ]----------------------------
interests | NULL
```

Oh no! Our records are `'string, list, items'`, so that won't work.


#### How about a function?

Our records are just strings. How about a [string function](#stringfunctions)?

```sql
SELECT split_part(interests, ',', '1')  -- #1
FROM my_contacts
WHERE interests IS NOT NULL;  -- #2
```

1. Split string at first `,`, return first part
2. We have some `NULL` values, so ignore those!

```text
-[ RECORD 1 ]----------------
split_part | RPG
-[ RECORD 2 ]----------------
split_part | RPG
...
-[ RECORD 10 ]---------------
split_part | women
```
