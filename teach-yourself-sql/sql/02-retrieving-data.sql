/* -----------------------------------------------------------------------------
   Retrieving Data
   =============================================================================
   By the end of this chapter you should have a good understanding of where this
   might be applied to the Taste-Token project. Don't write out all examples, as
   "Sams Teach Yourself SQL in 10 Minutes" is a good reference for this.

   1. Read the chapter
   2. Execute the examples
   3. Make notes (the best bits)
   4. Condense the notes (lazy loading)
   5. Make comments (avoid with obvious code)

    Notes
    -----
    1. Run `.help` to get available options
    2. SQL statements are not case sensitive (but names may be).
    3. SQL statements must end in a semicolon;
    4. SQLite does not show column names in query output (by default).
        - `.headers on` to display these
    5. If `ORDER BY` is missing, order of the rows is not guaranteed.
    6. Aim for readability, and your future stupid self!

    Questions
    ---------
    1. How to `count()` rows with a temporary `id` row?

*/

-- A single comment
SELECT * FROM Products;

-- You don't have to worry about CaSE sensITivitY
select * from products; -- 9 results

-- Listing unnecessary columns slows down performance (`*`)
SELECT prod_id, prod_name, prod_price FROM products;

-- Selecting w/out duplicates (applies to all columns)
SELECT DISTINCT vend_id FROM Products -- 3 results
SELECT DISTINCT vend_id, prod_price FROM Products; -- 6 results (collectively)

-- Limit the amount of results shown: start from row 6
-- SQL uses indexes from row `0` for our commands
SELECT prod_name FROM Products LIMIT 5 OFFSET 5