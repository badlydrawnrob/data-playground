## CASE statement

![When you want to switch genres, use CASE!](./img/genres.jpg)

### The problem

```text
----[ movie_tables ]----------------

| movie_id | title | rating | drama | comedy | ...
+----------+-------+--------+-------+--------+ ...
| ...      | ...   | ...    | False | True   | ...
```

1. Currently _genre_ headings are set to `True` or `False`
2. Some films belong to _more than one_ genre
    + Where should these films be shelved?
    + Adding `True` or `False` is time consuming and error-prone


### The solution

Dataville videos have decided to add a _category_ column. You _could_ add each film to the new category like this:

- If this category is `True`, set the category name to `category`
- `UPDATE table SET category = 'category' where category = 'True'`

As we've seen before **order is important** — if some films have _more than one_ genre set, it's `category` will be whichever `UPDATE` statement runs last.

#### There's a better way ...

Instead of running multiple `UPDATE` statements, we can do it all at once with `CASE`:

```sql
UPDATE my_table
SET new_column =             -- This is the column we're changing
CASE                         -- Run the below conditions on each row
  WHEN column1 = somevalue1  -- Does current row's `column1` equal this value?
    THEN newvalue1           -- It does? Set `column1` to new value
  WHEN column2 = somevalue2  -- ...
    THEN newvalue2           -- ...
  ELSE newvalue3             -- if no conditions met, set any value (not NULL!)
END;                         -- end the case statement
```


### Our new solution with CASE

```sql
UPDATE movie_table
SET category =
CASE
  WHEN drama = 'T' THEN 'drama'
  WHEN comedy = 'T' THEN 'comedy'
  ...
  ELSE 'misc'
END;
```

1. Only the first true condition will run!
2. If a film belongs to both `drama` and `comedy` ...
3. The `drama` value will be set ...
4. And will skip to the `END`


### Be careful with your conditions!

"End of the line" has an **R** rating — but! It is also a **cartoon**. Our `CASE` statement is going to make mothers angry:

```sql
UPDATE movie_table
SET category =
CASE
  WHEN cartoon = 'T' THEN 'family'
  ...
END;
```

Let's add a check for our `rating` column:

```sql
-- Only add a film to "family" category if it has a `G` rating!
...
CASE
  WHEN cartoon = 'T' AND rating = 'G' THEN 'family'  -- Only if
  ...
END;
```

### Where can I use CASE?

You can use `CASE` with `SELECT`, `INSERT`, `DELETE` and `UPDATE`!
