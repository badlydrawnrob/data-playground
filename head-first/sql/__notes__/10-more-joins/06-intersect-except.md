## INTERSECT and EXCEPT

![](./img/intersect-except.png)


### INTERSECT

```SQL
SELECT title FROM job_current
INTERSECT
SELECT title FROM job_desired;
```

Returns columns/records that are in **both** the first and second query.


### EXCEPT

```SQL
SELECT title FROM job_current
EXCEPT
SELECT title FROM job_desired;
```

Returns columns/records that are in the **_first_ query**, but _**not** the second_.
