## Transactions

![When your piggy bank screws up](./img/transactions.jpg)

You're the owner of the bank; three people are accessing their account at the same time, perhaps they're:

1. Checking their balance
2. Withdrawing cash
3. Moving cash between accounts

Let's take one of those examples:

1. Jack checks his account:
    + £`3000` available in account `A`
    + £`0` available in account `B`
2. Jack decides to move £`500` from account `A` to `B`
    + £`2500` in account `A`
    + £`0` in account `B`

That's not right! Unknown to Jack, there was a blackout in the branch — part of his transaction was lost:

```text
If account A >= 500
Subtract 300 from account A

==[ BLACKOUT! ]=============
Deposit 300 to account B    
============================
```

What happens if multiple accounts have the same problem? Or wires get crossed and mix up transactions? That's a lot of unhappy customers :(

### Complete or kill!

> A transaction is a group of query "steps". If one step fails, all steps fail.

We use the [classic ACID test](https://en.wikipedia.org/wiki/ACID_(computer_science)) to help us decide when to use an SQL transaction:

1. Atomicity
2. Consistency
3. Isolation
4. Durability

The following keywords help us perform a transaction:

1. `START TRANSACTION`: Keeps track of sql that follows
2. `COMMIT`: If nothing fails, we can make things permanent
3. `ROLLBACK`: If we have an error, it's as if nothing ever happened

[Postgres uses simpler syntax](https://www.postgresql.org/docs/current/tutorial-transactions.html), but it's essentially the same:


```SQL
-- Begin a transaction
BEGIN;
UPDATE accounts SET balance = balance - 100.00
    WHERE name = 'Alice';
    ...
ROLLBACK; -- Oops!

-- Commit a change
BEGIN;
UPDATE accounts SET balance = balance - 100.00
    WHERE name = 'Alice';
    ...
COMMIT;
```
