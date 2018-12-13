## Queries within Queries

![](./img/cats-in-box.jpg)

A _subquery_ is simply one query, inside another. It's helpful to:

- Search a growing database
- Pass one query (data set) to another query
- Look up one thing first, then perform manipulations
- Answer more than one question

```text
Which x is y
           ⤷ what Y = ?
```

You can use subqueries with `INSERT`, `DELETE`, `UPDATE`, and `SELECT`.

### Outer and inner query

- A subquery within another query is an _inner query_
- It's parent, is called an _outer query_


### Scalar values

A Subquery should generally [return a _scalar value_](https://www.youtube.com/watch?v=vb2sCy-ot9U)

- One query, one row, returning a _single value_


### Subqueries within subqueries

Can you write subqueries _inside_ subqueries? Yes! However, you should limit these wherever possible.
