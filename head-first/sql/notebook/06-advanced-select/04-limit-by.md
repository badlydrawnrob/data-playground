## LIMIT BY

<figure>

```text
--[ Total sales ]--

first_name | sales
-----------+-------
Britney    | 107.91
Nicole     | 98.23
Ashley     | 96.03
Lindsey    | 81.08
```

<figcaption>Fig. 1 — Displaying all girl guide's totals</figcaption>
</figure>

As Britney has aced every test we've searched for so far, we need to find a runner-up.

```sql
SELECT first_name, SUM(sales) AS sales
FROM cookie_sales
GROUP BY first_name  -- #1
ORDER BY sales       -- #2
LIMIT 2;          -- #3
```

1. Remember, we have to group our rows first!
2. If we stopped here, it would give us `fig. 1` (above)
3. We only need the "Top 2" girls, our winner and runner up
    + To achieve this, we `LIMIT` the number of results we'd like
    + Giving us `fig. 2`, below


<figure>

```text
-[ RECORD 1 ]-------
first_name | Britney
sales      | 107.91
-[ RECORD 2 ]-------
first_name | Nicole
sales      | 98.23
```

<figcaption>fig. 2 — List the winner and runner up</figcaption>
</figure>


### LIMIT BY and OFFSET

We only really need our second result here, to find our runner-up girl guide. We can `OFFSET` the results to achieve this:

```sql
SELECT first_name, SUM(sales) AS sales
FROM cookie_sales
GROUP BY first_name
ORDER BY sales
LIMIT 1 OFFSET 1;  -- Limit to a single result, skip the first row
```
