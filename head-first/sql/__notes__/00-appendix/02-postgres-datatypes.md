## Postgres datatypes

- [Basic overview](http://www.postgresqltutorial.com/postgresql-data-types/)
- [Full documentation](https://www.postgresql.org/docs/10/static/datatype.html)

### Character

| Type         | Description                                      |
| ------------ | ------------------------------------------------ |
| `CHAR(n)`    | fixed-length character (+ padded space if < `n`) |
| `VARCHAR(n)` | variable length character string (≤ `n`)         |
| `TEXT`       | variable (unlimited) length character string     |

### Numbers

| Type             | Description                                         |
| ---------------- | --------------------------------------------------- |
| `SMALLINT`       | integer with `range(-32,768, 32,767)`               |
| `INT`            | integer with `range(-2,147,483,648, 2,147,483,647)` |
| `SERIAL`         | integer (auto populate like `AUTO_INCREMENT`)       |
| `float(n)`       | floating point (n) precision                        |
| `real`           | double precision                                    |
| `numeric[(p,s)]` | Real number with (p) digits and (s) precision       |

Other types are available, such as `bigint` allowing more flexibilty.

### Temporal

| Type          | Description                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------------- |
| `DATE`        | stores data values only                                                                        |
| `TIME`        | stores the time of day values                                                                  |
| `TIMESTAMP`   | stores date and time values                                                                    |
| `TIMESTAMPTZ` | <abbr title="shorthand for timestamp with timezone">timezone-aware</abbr> date and time values |
| `INTERVAL`    | stores periods of time                                                                         |

### Other

See documentation for other datatypes, such as `arrays`, `json`, `uuid` and other special types.
