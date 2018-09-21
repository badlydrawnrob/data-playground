## String functions

[String functions](https://www.postgresql.org/docs/current/static/functions-string.html) for Postgres

1. Look for patterns
2. Make sure the pattern is the same for all values
3. Figure out which function to use to get the job done!
4. Functions return the modified originals: they _don't change_ the data

| Basic functions                  | Does this                                                            |
| -------------------------------- | -------------------------------------------------------------------- |
| `left(str, n)`                   | Return first _n_ characters in the string (see docs for `-n`egative) |
| `right(str, n)`                  | Return last _n_ characters in the string                             |
| `substr(string, from [, count])` | `substr('alphabet', 3, 2) -> 'ph'` (see docs)                        |
| `lower(string)`                  | Convert characters to lowercase                                      |
| `upper(string)`                  | Convert characters to uppercase                                      |
| `reverse(str)`                   | Return reversed string                                               |
| `length(str)`                    | Return the length of a string (characters)                           |
| `ltrim(str)`                     | Return string minus empty space from left (more options in docs)     |
| `rtrim(str)`                     | Return string minus empty space from right (more options in docs)    |


### Let's get atomic again!

Let's atomise our `locations` from Greg's `my_contacts` table:

```text
location      
-------------------
Palo Alto, CA
San Francisco, CA
San Diego, CA
Dallas, TX
Princeton, NJ
Mountain View, CA
```

#### Split a string

- `split_part(string text, delimiter text, field int)`

```sql
-- 1. split location
-- 2. at the comma
-- 3. return the first part
SELECT split_part(location, ',', 1) FROM my_contacts;
```
```text
location      
-------------------
Palo Alto
San Francisco
San Diego
Dallas
Princeton
Mountain View
```

#### Grab the county

- `right(str, n)`

```sql
-- 1. Grab 2 characters from the right
SELECT right(location, 2) FROM my_contacts;
```

```text
location      
-------------------
CA
CA
CA
TX
NJ
CA
```
