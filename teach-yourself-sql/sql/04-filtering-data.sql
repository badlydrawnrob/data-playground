/* -----------------------------------------------------------------------------
   Filtering Data
   =============================================================================
   Specify seach conditions

   Notes
   -----
   > Retrieve only the data you need with search criteria, also known as a
   > filter condition. This is using the `WHERE` clause, which should come before
   > the `ORDER BY` clause.

   Unlike in most programming languages, `=` (and not `==`) is used for equality.
   'Single quotes' are used to indicate the beginning and end of a string in SQL!

   Questions
   ---------
   1. What operators are available? (see the book, add to Anki)
   2. When to filter at the application level? (and not with SQL)
       - SQL to optimise performance (it's faster, reduce data transfer)
       - Application when it's highly dynamic (needs more flexibility)
   3. When do `NULL` values not show up in searches? (see pg.42 and chapter 06)
       - `NULL` isn't _like_ anything, it only equates to `NULL`!

*/

-- Search by exact price (only products with this price will show)
SELECT prod_name, prod_price
FROM Products
WHERE prod_price = 3.49;

-- 'Single quotes' are used for strings in SQL
SELECT vend_id, prod_name
FROM Products
WHERE vend_id != 'DLL01';

-- There's lots of equality tests to choose from!
-- `=  !=  <  <=  >  >=` and the following:
SELECT prod_name, prod_price
FROM Products
WHERE prod_price BETWEEN 1 and 4;

SELECT cust_name
FROM Customers
WHERE cust_email IS NULL;
--               IS NOT NULL