## ADD USER

Next, you'll want to [create a user](https://www.postgresql.org/docs/current/sql-createuser.html). This allows you to:

- Give full, or partial access
- Access without `root`
- Create multiple users

```SQL
CREATE USER username WITH ENCRYPTED PASSWORD 'password';
```

Create a different account for each person who'll access the database. You can then need to decide:

1. Who needs access?
2. How much access?
3. For what reasons?

Also consider their capabilities:

1. What is their level?
2. What is their experience?
3. Will they break anything?

It's better to be safe than sorry; easier to incrementally add access than remove it.
