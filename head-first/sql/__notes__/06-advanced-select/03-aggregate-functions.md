 ## Aggregate functions

![The girl guides are selling cookies. Who's in the lead?](./img/cookies.jpg)

```text
id | first_name | sales | sale_date  
----+------------+-------+------------
 1 | Lindsey    | 32.02 | 2007-03-12
 2 | Nicole     | 26.53 | 2007-03-12
 3 | Britney    | 11.25 | 2007-03-12
 . | ...        | ...   | ...
```
```sql
-- Find the highest individual sale
SELECT first_name, sales
FROM cookie_sales
ORDER BY sales;
```
```text
--[ Results ]--

"Britney", 43.2
"Britney", 34.1
"Lindsey", 32.0
...
```

### SUM() function

What's the total amount of sales for each girl guide?

```sql
-- We could group sales together by name ...
SELECT first_name, sales
FROM cookie_sales
ORDER BY first_name, sales;
```
```text
--[ Results ]--

"Ashley", 26.8
"Ashley", 19.2
...
"Britney", 43.2
"Britney", 34.1
...
```

It's nicely organised but we have to manually calculate totals. Let's find the `sum()` of Britney's sales:

```sql
SELECT sum(sales)
FROM cookie_sales
WHERE first_name = 'Britney';  -- Only sum() Britney's sales
```
```text
sum
---
107.91
```

#### GROUP BY and aggregate functions

There's an easier way. `GROUP BY` allows us to group rows together by a column.

```text
A -> GROUP BY column_name -> function(column_name) on this group -> Results
|
Z -> GROUP BY column_name -> function(column_name) on this group -> Results
```


#### SUM() and GROUP BY

If we want to find the total of all our girl guides, we'd need to:

1. Find the `sum()` of each girl guides sales
    + By using the `sum()` function on `sales` column
2. Group each girl guide by their `first_name`
    + Which includes all her sales rows
    + Add each row for the current girl guide
    + Find her total with the `sum()` function (mentioned in step #1)
3. Order the results in reverse (largest first)
    + <i>You must use the same column / aggregate function!</i>

```sql
SELECT first_name, sum(sales)  -- #1
FROM cookie_sales
GROUP BY first_name            -- #2
ORDER BY sum(sales) DESC;      -- #3
```
```text
-------------------------------------------[ order by sales ]----
A -> GROUP BY first_name -> Total sales -> | { "Britney", 107.91 }
|                                          | { "Nicole", 98.23 }
Z -> GROUP BY first_name -> Total sales -> | { "Ashley", 96.03 }  
```  

##### An easier way to order with aggregate functions

We can give the column (and it's aggregate function) an alias [**#1**] — similar to naming a variable. This will also rename our sales column in the output:

```sql
SELECT first_name, sum(sales) AS total_sales  -- #1
FROM cookie_sales
GROUP BY first_name
ORDER BY total_sales DESC  -- #1 ... Ditto!
```
```text
--[ Results ]-----------

first_name | total_sales
-----------+------------
Britney    | 107.91
Nicole     | 98.23
Ashley     | 96.03
Lindsey    | 81.08
```


### AVG() and GROUP BY

We could also work out each girls average (over 7 days):

```sql
SELECT first_name, AVG(sales) AS average_sales  -- #2
FROM cookie_sales
GROUP BY first_name  -- #1
ORDER BY average_sales DESC;  -- #3
```

1. Group each girl guides sales by `first_name`
2. Calculate each girl's average sales (`sum(sales) / number of days`)
3. Order by our new `average_sales` column (highest first)


```text
--[ Results ]----------------

first_name | average_sales
-----------+-----------------
Britney    | 15.4157142857143
Nicole     | 14.0328571428571
Ashley     | 13.7185714285714
Lindsey    | 11.5828571428571
```


### MIN() or MAX() and GROUP BY

We could also look for the _`min()`imum_ or _`max()`imum_ sales for each girl guide, to see which girl had the most (or least) sales on a single day:

```sql
SELECT first_name, MAX(sales) AS max_sale  -- Or replace with min()
FROM cookie_sales
GROUP BY first_name;
```
```text
--[ Results ]----------------

first_name | max_sale
-----------+-----------------
Lindsey    | 32.02
Britney    | 43.21
Nicole     | 31.99
Ashley     | 26.82
```

### COUNT()

`count()` returns the number of rows in a given column:

```sql
SELECT COUNT(sale_date)  -- Will return number of rows (28)
FROM cookie_sales;
```

If we wanted to see how many days each girl sold cookies, we could try this:

```sql
SELECT first_name, COUNT(sale_date)  -- #1
FROM cookie_sales
WHERE sales > 0       -- #2
GROUP BY first_name;  -- #3
```

1. We don't have to include `first_name`, but let's display
2. Generally you'll want to remove `0` values from results
    + Only return days when `sales` were _more than_ `0`
3. Grouping by `first_name` links `sale_date` rows to each girl

```text
-- Daaamn girl, you still be on top

first_name | count
-----------+-------
Lindsey    |     6
Britney    |     7
Nicole     |     6
Ashley     |     6
```

#### COUNT() and SELECT DISTINCT

We might like to know for sure how many days the girls were out selling cookies (even if they didn't make a sale!)

- We could `ORDER BY` the `sale_date`
    + But there might be tons of entries
    + And we might get the calulation wrong
- It's far easier to _select_ all the _distinct_ rows


```text
--[ SELECT DISTINCT rows ]--

x -> | x
y -> | y
z -> | z
z -> |
y -> |
x -> |
```

```sql
SELECT DISTINCT sale_date  -- No duplicates!
FROM cookie_sales          
ORDER BY sale_date;  -- Earliest date first!
```
```text
sale_date  
------------
2007-03-06
2007-03-07
2007-03-08
2007-03-09
2007-03-10
2007-03-11
2007-03-12
(7 rows)
```

We can use our `COUNT()` function to return the number of distinct rows!

```sql
SELECT COUNT(DISTINCT sale_date) -- DISTINCT goes inside the function
FROM cookie_sales; -- Only returns one value, no need to ORDER BY
```

Now let's add that our original [count()](#count) for the girls:

```sql
SELECT first_name, COUNT(sale_date)
FROM cookie_sales
WHERE sales > 0
GROUP BY first_name;
```

- This will return exactly the same result as before (Britney wins again!) ...
- But we can be certain it returns ONLY ONE of a particular `sale_date`
    + If a girl had two records (or rows) for the same day, one would be ignored
    + This helps us quickly see the variety of values in _any_ column (ignoring duplicates)


#### COUNT() and DISTINCT — Another way!

For small tables, the above method works. In big tables, [you're gonna have problems my friend](https://stackoverflow.com/a/14732410) ...

```sql
SELECT COUNT(*)
FROM (
  SELECT DISTINCT sale_date
  FROM cookie_sales
) AS total_days;
```

This will give you exactly the same results, quicker. It's called an _inner select_.
