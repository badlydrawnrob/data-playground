## Leftovers

Excerpts from _The Top Ten Topics we didn't cover_.

1. Get a GUI
2. Reserved words and special characters
3. [`ALL`, `ANY`, `SOME`](https://www.postgresql.org/docs/current/functions-comparisons.html)
4. [Data types](https://www.postgresql.org/docs/current/datatype.html)
5. [Temporary tables](http://www.postgresqltutorial.com/postgresql-temporary-table/)
6. [`CAST` or `::`](http://www.postgresqltutorial.com/postgresql-cast/) to convert one data type to another
7. Current user, time or date `SELECT CURRENT_[USER | TIME | DATE]`
8. [Useful numeric functions](https://www.postgresql.org/docs/current/functions-math.html) (probably best to just use Python!)
9. [Indexing](https://devcenter.heroku.com/articles/postgresql-indexes) to speed things up

You'd probably also be wise to _use an ORM_ for most of the heavy lifting.

1. Use the easiest method possible
2. Test speed as you go
3. Identify bottlenecks and improve performance
