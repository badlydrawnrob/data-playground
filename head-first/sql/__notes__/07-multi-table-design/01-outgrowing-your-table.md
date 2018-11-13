## Outgrowing your table

![Often, it's best to split your data into multiple tables!](./img/nested-tables.jpg)

It's likely you'll outgrow a single 1NF table, for any number of reasons, but the main ones being:

1. It's too hard to query specific results
2. Your queries are getting too complicated
3. You've got redundant, or repetitive data

So if you have a query like the one below — it's time to split data into more than one table!

```SQL
-- Our contact
{
  'id': 341,
  'first_name': 'Moore',
  'interests': 'animals, horseback riding, movies',
  ...
}
-- Find him a lady with the same interests
SELECT * FROM my_contacts
WHERE gender = 'F'
AND status = 'single'
AND state = 'TX'
AND seeking LIKE '%single M%'
AND birthday > '1970-08-28'
AND birtday < '1980-08-28'
AND interests LIKE '%animals%'
AND interests LIKE '%horse%'
AND interests LIKE '%movies%';
-- Sooo many conditions :(
```




### Letting your table do the work

```text
--[ bad design ]--

contact | interest_1 | interest_2 | ...
--------+------------+------------+----
1       | True       | False      | ...
2       | False      | True       | ...

--[ good design ]--

contact | interest
--------+---------
1       | 5       
2       | 6

          id  | interest
          ----+---------
          ... | ...
          5   | cycling
          6   | films
          ... | ...
```

In the example above, we list each contact's interests. In a real world example, each contact would have multiple interests, so we need to figure out a sane way of structuring that information — making sure we can easily `SELECT` any contact we want based on this information.


Bad table design         | Good table design
-------------------------|------------
complex `selects`        | easy `selects`
bad matches              | correct matches
search too complex       | it just works
hacks/workarounds        |
