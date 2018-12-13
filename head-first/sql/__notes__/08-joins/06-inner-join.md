## Inner join

![](./img/inner-join.png)

An _inner join_ combines records from two tables, using _comparison operators_ in a _condition_:

```sql
SELECT somecolumns
FROM table1
  INNER JOIN
    table2
ON somecondition;
```

You can use `GROUP BY`, `ORDER BY`, `WHERE`, and functions with a `JOIN` — just like a regular `SELECT`!

### Equijoin

Equijoin inner joins test for equality — here, we're matching foreign key to a primary key:

```sql
SELECT somecolumns
FROM table1 AS t1
  INNER JOIN
    table2 AS t2
ON t1.id = t2.id
```

If we had a table of boys with one toy each, and a one-to-one relationship with a table of toys an equijoin would give us the following results:

```text
id | boy    | toy_id       toy_id | toy
---+--------+-------       -------+-----
1  | Davey  | 3            1      | hula hoop
2  | Bobby  | 5            2      | balsa glider
3  | Beaver | 2            3      | toy soldiers
...                        ...
```
```text
-[ RECORD 1 ]-------
boy | Richie
toy | hula hoop
-[ RECORD 2 ]-------
boy | Billy
toy | balsa glider
-[ RECORD 3 ]-------
boy | Beaver
toy | balsa glider
-[ RECORD 4 ]-------
boy | Davey
toy | toy soldiers
-[ RECORD 5 ]-------
boy | Johnny
toy | harmonica
-[ RECORD 6 ]-------
boy | Bobby
toy | baseball cards
```

### Non-equijoin

You can use the _not equal to_ (`<>` or `!=`) returns the toys each boy _doesn't_ have:

```sql
SELECT boys.boy AS boy, toys.toy
FROM boys
  INNER JOIN
  toys
ON boys.toy_id <> toys.toy_id
ORDER BY boy;
```
```text
-[ RECORD 1 ]-------
boy | Beaver
toy | baseball cards
-[ RECORD 2 ]-------
boy | Beaver
toy | etch-a-sketch
-[ RECORD 3 ]-------
boy | Beaver
toy | harmonica
-[ RECORD 4 ]-------
boy | Beaver
toy | toy soldiers
-[ RECORD 5 ]-------
boy | Beaver
toy | slinky
-[ RECORD 6 ]-------
boy | Beaver
toy | tinker toys
-[ RECORD 7 ]-------
boy | Beaver
toy | hula hoop
-[ RECORD 8 ]-------
boy | Billy
...
```
