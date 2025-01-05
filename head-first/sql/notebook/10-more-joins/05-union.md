## UNION

![](./img/union.png)

`UNION` allows you to merge two or more sets, returning common values:


```text
{'designer', 'dentist'} =>
{'nurse', 'designer'}   =>  {'designer', 'dentist', 'manager', 'nurse'}
{'manager'}             =>
```
```SQL
SELECT title FROM job_current
UNION
SELECT title FROM job_desired
UNION
SELECT title FROM job_listings;
```
```text
title
--------
designer
dentist
manager
nurse
```

### Limitations

Each `SELECT` query must have:

- Same number of columns
- Same datatype


### UNION ALL

To show _every single_ record from each `SELECT` — *including* duplicates — use `UNION ALL`.
