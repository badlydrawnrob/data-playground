## Migrate our data

We're using a [string function](#stringfunctions) to select our data. Let's migrate it into our new `interests` table. One way is to:

1. Create new columns
2. Split our `string, list` into atomic data
3. Add each list item into it's own column
4. Migrate each column into our new `interests` table

```sql
ALTER TABLE my_contacts
ADD COLUMN interest1 character varying(50),
ADD COLUMN interest2 character varying(50),
ADD COLUMN interest3 character varying(50),
ADD COLUMN interest4 character varying(50);
```
```text
interests  | RPG, kayaking
interest1  | NULL
interest2  | NULL
interest3  | NULL
```

We can now copy and paste `interests` first item into `interest1` ...

```sql
UPDATE my_contacts
SET interest1 = split_part(interests, ',', 1);
```
```text
interests | RPG, kayaking
interest1 | RPG
```  

Now you can delete that first item from `interests`!

```sql
UPDATE my_contacts
SET interests = substr(interests, length(interest1) + 2 + 1)  -- #1

UPDATE my_contacts
SET interests = NULL;
```

1. `substr(...)` returns a portion of the string
    + `|R|P|G|,| |K|a|y|a|k|i|n|g|` row has 13 characters
    + We want to return `Kayaking`
    + Our _position start_ should be `6`
        - Take the length of `RPG` (now in `interest1`)
        - Plus `2` (the comma and space)
        - Add `1` (to move our imaginary cursor to `K`)
    + Returns _position_ 6, to end.
2. `NULL` our old `interests` column (we'll delete it later)

```text
interests | kayaking
interest1 | RPG
```

Repeat the process for the remaining `interests` list items, moving into `interests2`, `interests3`. Remember to ignore your new `NULL` values!


### We're not quite done yet!

We can view all our interests with a little digging ...

```sql
SELECT
  interest1,
  interest2,
  interest3
FROM my_contacts
WHERE
  interest1 IS NOT NULL
  OR interest2 IS NOT NULL
  OR interest3 IS NOT NULL;
```

But we can't easily pull these out into a single results set. We need a way to merge them.
