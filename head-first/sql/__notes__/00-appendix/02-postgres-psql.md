## PSQL

| Documentation |                                        |
| ------------- | -------------------------------------- |
| `help`        | intro guide                            |
| `\?`          | help options for psql commands         |
| `\h`          | help for sql commands (`\h [command]`) |



| Basic commands       |                                  |
| -------------------- | -------------------------------- |
| `\q`                 | quit PSQL (`quit` in #11)        |
| `\l`                 | list all databases               |
| `\du`                | list user roles                  |
| `psql -U [username]` | connect with a specific username |



| Connect to database |                                                  |
| ------------------- | ------------------------------------------------ |
| `\c [database]`     | connect to database                              |
| `\dt`               | Lists all tables                                 |
| `\d` or `\d+`       | `\d [table_name]` display table, constraints etc | 
| `q`                 | Exit list                                        |



| The query buffer |                                       |
| ---------------- | ------------------------------------- |
| `\p`             | show the contents of the query buffer |
| `\r`             | reset (clear) the query buffer        |
| `\s [FILE]`      | display history or save it to file    |



| Export database |                                      |
| --------------- | ------------------------------------ |
| `pg_dump`       | `pg_dump [database] > [to_filename]` |



| Nice extras |                                  |
| ----------- | -------------------------------- |
| `\x [auto]` | enter/exit expanded display mode |
