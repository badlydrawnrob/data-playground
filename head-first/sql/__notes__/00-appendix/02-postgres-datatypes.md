## Postgres datatypes

- [Basic overview](http://www.postgresqltutorial.com/postgresql-data-types/)
- [Full documentation](https://www.postgresql.org/docs/10/static/datatype.html)


### Character

| Type         | Description                                      |
| ------------ | ------------------------------------------------ |
| `char(n)`    | fixed-length character (+ padded space if < `n`) |
| `varchar(n)` | variable length character string (≤ `n`)         |
| `text`       | variable (unlimited) length character string     |

### Numbers

| Type             | Description                                         |
| ---------------- | --------------------------------------------------- |
| `smallint`       | integer with `range(-32 768, 32 767)`               |
| `int`            | integer with `range(-2 147 483 648, 2 147 483 647)` |
| `serial`         | integer (auto populate like `AUTO_INCREMENT`)       |
| `real`           | double precision                                    |
| `numeric[(p,s)]` | Real number with (p) digits and (s) precision  (alias: `decimal`)      |

Other types are available, such as `bigint` allowing more flexibilty.

### Temporal

| Type          | Description                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------------- |
| `date`        | stores data values only                                                                        |
| `time`        | stores the time of day values                                                                  |
| `timestamp`   | stores date and time values                                                                    |
| `timestampz` | <abbr title="shorthand for timestamp with timezone">timezone-aware</abbr> date and time values |
| `interval`    | stores periods of time                                                                         |

### Other

See documentation for other datatypes, such as `arrays`, `json`, `uuid` and other special types.
