## Postgres commands

- Commands to use with: https://postgresapp.com
- Enable `psql` on your `.bash_profile`
- You can also search how to set up [`psql` config](https://do.co/2x7vKuD)


### PSQL

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



| Connect to database |                                 |
| ------------------- | ------------------------------- |
| `\c [database]`     | connect to database             |
| `\dt`               | Lists all tables                |
| `\d`                | `\d [table_name]` display table |
| `q`                 | Exit list                       |



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


-----

### User roles and privileges

#### Create user

`CREATE USER [username] WITH ENCRYPTED PASSWORD '[password]';`

#### Change password

`ALTER USER [username] WITH ENCRYPTED PASSWORD '[password]';`

#### User privileges (roles)

`GRANT ALL PRIVILEGES ON DATABASE [dbname] TO [username];`

#### Live server

1. Create a super user
2. Login as super user `postgres`
3. Follow the above to create a user and give privileges
4. **Never use root** (`postgres`) to connect to the database on your app
