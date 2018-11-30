## Cartesian join

![**Cartesian product of two sets:** tables A and B have `2 * 2` or `6` possible combinations](./img/cartesian-product.png)

- Also known as the _cartesian product_
- Returns _all_ possible combinations of rows, from two (or more) tables
- Can help you fix bugs in your joins (if you accidentally get cartesian results)
- Test the speed of your RDBMS and it's configuration
- **DO NOT** use on large datasets — it could kill your machine

It can be written like this in SQL:

```sql
SELECT a.animal, b.ingredient
FROM animal AS a
  CROSS JOIN
  breakfast AS b;

-- or

SELECT a.animal, b.ingredient
FROM animal a, breakfast b;
```
