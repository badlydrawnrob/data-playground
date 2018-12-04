## Outer join

![Outer join set theory illustration]()

You've seen an _inner join_ before. Another tool in your belt is the _outer join_.


**NEEDS MUCH BETTER EXPLAINATION!**

An inner join:

Matches `row a` (key) in `table a`
with `row b` (key) in `table b`


An outer join:

Matches ALL rows in `table a`
with rows in `table b`

Returns `NULL` values on `table a` (that do not have matches or entries on `table b`)


### Left and right joins

A _left outer join_ matches `table a`, against `table b`

![sketch match `A` against `B`]


A _right outer join_ matches `table b` against `table a`


It's generally best to **stick to one** and switch the actual tables instead.
