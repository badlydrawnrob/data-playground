## User privileges

Below are some of the commands you'll find yourself using with new users — **read the docs** and tutorials! It's best to learn as you go, only adding what you need.

- [`GRANT`](https://www.postgresql.org/docs/current/sql-grant.html) access
    - For example, allow them to `SELECT` or `INSERT`
    - But _not_ `DELETE` rows
- [`REVOKE`](https://www.postgresql.org/docs/current/sql-revoke.html) access
    - `CASCADE` the changes
    - `RESTRICT` the changes
- [`CREATE ROLE`](https://www.postgresql.org/docs/current/sql-createrole.html)
    - `DROP` and remove it
