## 1NF

We first need to make sure we're in _first normal form_

1. Each row of data must contain atomic values
2. Each row of data must be unique
3. Values stored in a column should be of the same type
4. No repeating types of data across columns
5. Columns should have unique names
6. Order of data stored doesn't matter


#### Composite key

![](./img/normalisation-1nf.jpg)

In this example, we've made the data atomic and split the tables — however, the second column needs a little work. It has duplicate data in the rows. To fix this, we can use a **composite key**

- A composite key is a primary key using multiple columns

So, if we combine the `toy_id` and it's `color`, we'll have our _composite key_ and each row will be unique!


#### Functional dependency

```text
--[ Superheroes ]-----------
name            | Super Guy
power           | Flies
...             | ...
initials        | SG
arch_enemy_id   | 4
arch_enemy_city | Kansas City  
```

1. **Composite key**: `name` and `power`
2. **Functional dependency**: `initials`

`initials` are _functionally dependent_ on `name`; they'll change if our superhero `name` does!

> A dependent column is one containing data that could change if another column changes


##### Partial functional dependency

The `initials` column is _partially_ dependent on `name`. Partial dependency means one _non-key_ column is reliant on some, but not all, of the columns in a composite primary key.


##### Transitive functional dependency

How does each _non-key_ column relate to others? If our `arch_enemy_id` changes, it _could_ potentially change the `arch_enemy_city` field. If it could potentially change one of the other (non-key) columns, it's called a _transitive functional dependency_.

##### Independent

Your column can also be independent. For instance, if `arch_enemy_city` is not dependent on `arch_enemy_id` or any other column.

- If you changed a row in your column, would anything else change? No?
- Your column is independent!


#### Avoiding dependencies

You'll generally avoid dependencies by making sure all tables have a unique primary key. There are some good arguments for both a _synthetic key_ and a _natural key_. Google it!
