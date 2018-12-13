## Subquery steps

To solve a subquery:

1. Split into steps
2. What questions are you asking the database?
3. What data is required for each step?
4. Write the query

Finally, you'll combine the queries together with the `WHERE` clause.



### Subquery vs join

![An example of a subquery and a join — both give the same result!](./img/subquery-vs-join.jpg)

You often get faster results by using a `JOIN` (or `LIMIT`) _instead_ of a subquery. Most subqueries can be replaced and return the same data; you'll need to ask yourself:

- Which method is faster? (experiment)
- Does it need to be fast? (local/live)
- Which is easiest to read?
- Is it simpler to use?

Make the query as _easy as possible_ for your database to answer. Write what makes logical sense first, and worry about performance later.



### What are the benefits?

- It can sometimes be faster
- You don't explicitly need to know the value
    `x > SELECT`, rather than hardcoding the value to compare
