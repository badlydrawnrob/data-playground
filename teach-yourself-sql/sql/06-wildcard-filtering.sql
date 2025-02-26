/* -----------------------------------------------------------------------------
   Using wildcard filtering (slower than other filters)
   =============================================================================
   Wildcard searches are a broader (catch-all) type of search. These are for
   times when you might not know exactly what you're looking for! Wildcards are
   special characters used to match parts of a value. Take care when using
   wildcards as THEY CAN BE SLOW (search patterns that begin with wildcards
   are the slowest to process!)

   Notes
   -----
   > SQLite doesn't seem to be CASE SENSITIVE but some providers are.
   > We must use the `LIKE` operator (predicate), for wildcards to work.
   > It can only be used with text fields (strings).

   1. `%` represents ZERO, ONE, or more characters.
   2. `_` underscore represents exactly ONE character.
   3. `GLOB` is also used like `[JM*]' or `[^JM*]' for unix style wildcards
       - This is CASE SENSITIVE in SQLite!
   4. Watch out for leading or trailing spaces (which should be avoided)
   5. `NULL` will never be matched, obviously.

   Questions
   ---------
   1. Some databases pad field contents with spaces (to fill max chars)
       - I don't think SQLite does this (see book for solution)
   2. How do I do `[]` set of characters in SQLite?
       - Use `GLOB` instead

*/

-- Match any number of occurences of any character
-- e.g: all words that begin with the word "Fish"
SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE 'Fish%'; -- may be case sensitive (not in SQLite)

-- Wildcards can be used anywhere in the search pattern ...
SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE '%bean bag%'; -- returns any value that contains this text!

-- This is less useful than above, but you can search within words ...
SELECT cust_email
FROM Customers
WHERE cust_email LIKE 'j%@fun4all.com'; -- jjones@fun4all.com
-- WHERE prod_name LIKE 'F%y'; -- 'Fish bean bag toy'

-- Search by characters (a single character using `_` underscore)
SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE '__ inch teddy bear'; -- two spaces, two chars

-- `GLOB` can be used instead of `LIKE` for sets of characters (UNIX wildcards)
-- To negate the wildcard you can use `'[^JM]*'` (not beginning with)
SELECT cust_contact
FROM Customers
WHERE cust_contact GLOB '[JM]*' -- any name beginning with 'J' or 'M' (case sensitive)
ORDER BY cust_contact;