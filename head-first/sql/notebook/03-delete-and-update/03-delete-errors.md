## DELETE errors

![Fizzy pop rots your teeth. A bad `DELETE` statement rots your data!](./img/fizzy-pop.jpg)

It's a good idea to double (and triple!) check your `DELETE` statements before running them. Make sure you're only deleting the rows you want:

- A typo could give unintended consequences ...
- Ditto for records that share values ...
- Or the order you run them!


### Don't rot your data!

Imagine you need to change the prices of two cans of coke:

```sql
-- {'pepsi': 1.00, 'coca cola': 1.50}

-- Update the pepsi price
INSERT INTO fizzy_drinks
VALUES ('pepsi', 1.50);
-- Now delete the old value
DELETE FROM fizzy_drinks
WHERE price = 1.50;
```

But wait ... now we have two cans of coke the same price:

- if we delete the `1.50` drinks ..
- we'd accidentally delete both our cans of coke
