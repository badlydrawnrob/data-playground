/* -----------------------------------------------------------------------------
   Sorting Retrieved Data
   =============================================================================
   These commands help us to organise our results.

   Notes
   -----
   > Data is by default stored in the way it was entered, but this may be changed
   > if data is updated or deleted. Don't rely on the natural sorting order!

   Questions
   ---------
   1. Which comes first: `A` or `a`? `B` or `z`?
   2. What about special characters?
   3. What about foreign languages?

*/

-- Order by defaults to ABC ascending (clause should come last)
SELECT prod_name FROM Products ORDER BY prod_name;

-- Order by more than one column (you can also number the columns `2, 3`)
SELECT prod_id, prod_price, prod_name FROM Products
ORDER BY prod_price, prod_name; -- `a` is only sorted if `b` has same values!

-- To reverse the order CBA you add a keyword
SELECT prod_id, prod_price, prod_name
FROM Products
ORDER BY prod_price DESC, prod_name; -- order by price, then by name (ABC)

