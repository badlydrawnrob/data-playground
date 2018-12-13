## Outer join

![](./img/outer-join.png)

You've seen an _inner join_ before. Another tool in your belt is the _outer join_.


### An inner join:

- `row a` in `table a` matches to ...
    + `row b` in `table b`

Returns exact matches between `table a` and `table b`, using a matching _primary key_ or _id_


### An outer join:

- rows in `table a` match to ...
    + rows in `table b`
        + even if there's `NULL` matching result

Returns exact matches between `table a` and `table b` — also returns `NULL` values if no matching _primary key_ or _id_ can be found on `table b`.


### Left and right joins

![](./img/outer-join-example.png)

| Left outer join | Right outer join |
|-----------------|------------------|
| ![](./img/left-outer-join.png)  | ![](./img/right-outer-join.png)  |
| A _left outer join_ matches `table a`, against `table b`  | A _right outer join_ matches `table b` against `table a`  |

It's generally best to **stick to one** and switch the actual tables instead.
