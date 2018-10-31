## ORDER BY statement

![](./img/order.jpg)

Our Dataville movies are getting messy. There are many ways to organise them:

1. By title
2. By rating
3. By category
4. A mix of these

To order by title, it'd look something like:

```sql
SELECT title, category_type
FROM movie_list
ORDER BY title;  -- Pick a column in the SELECT
```

- Lists in `ASC`ending order [A-Z, default]
    + Films with numbers come first
    + Characters listed alphabetically
- You can also list in `DESC`ending order [Z-A]

```sql
SELECT title, category_type
FROM movie_list
WHERE category = 'family'  -- Limit results to a genre
ORDER BY title DESC;       -- Reverse the list order
```

You can also pick the column with a number:

```sql
SELECT title, category_type
...
ORDER BY 1 ASC;  -- maps to `title`
```

### ORDER BY multiple columns

Dataville want to see which films are too old:

```sql
SELECT title, category_type, purchased  -- #1
FROM movie_list
ORDER BY category_type, purchased;  -- #2, #3
```

1. Grab the date it was `purchased`
2. List _all_ films, ordered by category
3. Then order them by purchase date


#### ORDER BY sorts from left to right

You'll notice films are ordered by _purchase date_, not alphabetically.

```text
A --> Sort by category --> Sort by purchase date { alpha, '2008', auto, '2012' }
|
Z --> Sort by category --> Sort by purchase date { zelda, '2001', zappo, '2002' }
```

Let's add `title` as the last column to sort:

```sql
SELECT title, category_type, purchased
FROM movie_list
ORDER BY category_type, purchased, title;  -- #1, #2, #3
```

1. Order by `category_type`
2. Then by `purchase` date
3. Finally by their `title`

```text
-- Categories beginning with A
-- #3                      #1              #2

| title                  | category_type | purchased |
+------------------------+---------------+-----------+
| Greg: the untold story | Action        | 2001      |
| Take it back           | Action        | 2003      |
| ...                    | ...           | ...       |
```
