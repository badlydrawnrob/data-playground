## UPDATE statement

![It's easier to update than do things manually](./img/update-iphone.jpg)

The `UPDATE` statement simply "updates" the value you want, in the place you need. It's much easier than the _SELECT-INSERT-DELETE_ combo:

- You `SET` a `column_name` to (equal) a new `'value'`
- You use `WHERE` to get specific — just like `SELECT` and `DELETE`!

```sql
-- Original: {'pepsi': 1.00}
UPDATE fizzy_pop
   SET price = 1.50
 WHERE name = 'pepsi';

-- Result: {'pepsi': 1.50}
```

### More than one column (or row)

You can set multiple columns, and multiple rows (depending on your `WHERE` statement)

```sql
UPDATE fizzy_pop
   SET price = 1.50,
       name = 'super pepsi'
 WHERE name = 'pepsi';
```

### Remember our fizzy pop dilemma?

You also need to be careful about order in an `UPDATE` statement:

```sql
-- {'pepsi': 1.00, 'coca cola': 1.50}

-- Update the pepsi price
UPDATE fizzy_pop
   SET price = 1.50
 WHERE price = 1.00

-- Now update the price of coca cola
UPDATE fizzy_pop
   SET price = 2.00
 WHERE price = 1.50

-- {'pepsi': 2.00, 'coca cola': 2.00}
```

**WTF** happened there?

1. When we changed `'pepsi'`, it's now the same price as `'coca cola'`
2. So our second `UPDATE` now also targets `'pepsi'`. Oops!
3. The solution is to _reverse the order_ (highest price first)


### There's an easier way ...

We can use simple maths on numeric values — throw in an `OR` and we can do it all in one simple `UPDATE`!

```sql
-- {'pepsi': 1.00, 'coca cola': 1.50}
UPDATE fizzy_pop
   SET price = price + 0.50
 WHERE name = 'pepsi'
    OR name = 'coke';
-- {'pepsi': 1.50, 'coca cola': 2.00}
```

**Important:** Make sure you always include a `WHERE` statement, or you'll update _all_ your rows!
