/* -----------------------------------------------------------------------------
   Advanced data filtering
   =============================================================================
   Here we'll be combining `WHERE` clauses and learning to search `In` for ranges
   of conditions. We'll be using `AND` `OR` conditional operators too. It's entirely
   likely that the order of results will be slightly different to the book without
   `ORDER BY`.

   Notes
   -----
   > Don't rely on the order of `AND` and `OR` operators, use parentheses.

   1. You've got to be careful which expressions are evaluated first.
   2. Parenthesis help group expressions together, and makes for easier reading!
   3. Everything within parenthesis gets interpreted FIRST.

   Questions
   ---------
   1. Why use `IN` instead of `OR`?
       - It's more efficient, and easier to read
       - It can contain another `SELECT` statement (see chapter 11)
   2. Why use `NOT` when you can use `!=`?
       - `NOT` can sometimes be more readable
       - It can be used in more complex clauses, like `IN` and `BETWEEN`

*/

-- Filter search by string and number (order by CBA)
SELECT prod_id, prod_price, prod_name
FROM Products
WHERE vend_id = 'DLL01' AND prod_price <= 4
ORDER BY prod_name DESC;

-- Filtering search with multiple conditions: ORDER MATTERS!
-- 1. "This or that ID", then "this price" (with parenthesis)
-- 2. "That ID and this price", then "this ID" (without parenthesis)
SELECT prod_name, prod_price
FROM Products
WHERE (vend_id = 'DLL01' OR vend_id = 'BRS01') -- runs first
      AND prod_price >= 10; -- runs second

-- `IN` takes a comma-separated list of values (range of conditions)
-- this will return the same results as `OR` with `vend_id`s
SELECT prod_name, prod_price
FROM Products
WHERE vend_id IN ('DLL01', 'BRS01');

-- Negate a condition with `NOT` (return everything that is not x)
SELECT prod_name, prod_price
FROM Products
WHERE vend_id NOT IN ('DLL01', 'BRS01');
-- WHERE NOT vend_id = 'DLL01'; -- is the same as:
-- WHERE    != vend_id 'DLL01';