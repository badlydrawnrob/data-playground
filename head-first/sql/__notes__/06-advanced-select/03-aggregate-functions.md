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
