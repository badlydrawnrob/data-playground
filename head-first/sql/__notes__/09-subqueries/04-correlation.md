## Correlation

### Non-correlated subquery

```SQL
-- example of non-correlated
```

An inner query that **is not** referenced in the outer query.

- `Y` doesn't know about outer query `X` (it's a single value)
- But `X` is dependant on the result of `Y`

Here, the inner query is processed first.


### Correlated subquery

```SQL
-- example of subquery in a select column
```

A correlated subquery **does** reference the outer query.

- `Y` is dependant on the outer query `X`
    - i.e: reference a column alias within subquery
