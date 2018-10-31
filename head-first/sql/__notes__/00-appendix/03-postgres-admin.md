## User roles and privileges

### Create user

`CREATE USER [username] WITH ENCRYPTED PASSWORD '[password]';`

### Change password

`ALTER USER [username] WITH ENCRYPTED PASSWORD '[password]';`

### User privileges (roles)

`GRANT ALL PRIVILEGES ON DATABASE [dbname] TO [username];`

### On a production server

Be careful! Always keep things secure.

1. Create a super user
2. Login as super user `postgres`
3. Follow the above to create a user and give privileges
4. **Never use root** (`postgres`) to connect to the database on your app
