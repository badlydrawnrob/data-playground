## Postgres commands

### PSQL

| Command | Does this                            |
| ------- | ------------------------------------ |
| `help`  | Help options                         |
| `\h`    | `\h`elp + `COMMAND` reveals help doc |
| `\q`    | `\q`uit PSQL                         |
| `\l`    | `list` all databases                 |
| `\c`    | `\connect [database]`                |
| `\du`   | List user roles                      |


### Connected to database

| Command | Does this                       |
| ------- | ------------------------------- |
| `\dt`   | Lists all tables                |
| `\d`    | `\d [table_name]` display table |
| `q`     | Exit list                       |


### Exporting database

| Command   | Does this                            |
| --------- | ------------------------------------ |
| `pg_dump` | `pg_dump [database] > [to_filename]` | 
