## Aliasing

You can think of the `AS` keyword as a variable. It stores the value of `X` as the alias `Y`.

- An alias is _temporary_
    + It displays in your results ...
    + But _doesn't_ change original values
- It helps to _simplify_, and make values _easy to read_
- You can alias _without_ using `AS`
    + Just remove the `AS` keyword!
    + It sometimes makes things clearer to use it, though


### Column aliases

You've seen these before. `AS` allows us to store the value of a column:

```sql
CREATE TABLE profession (
  id SERIAL,
  profession varchar(20)
) AS
  SELECT profession AS mc_prof  -- #1
  FROM my_contacts
  GROUP BY mc_prof
  ORDER BY mc_prof;
```


### Table aliases

- Also known as _correlation names_.
- Help when you're selecting data from more than one table
- Reduces finger fatigue (no typing table names over and over!)

```sql
SELECT profession mc_prof
FROM my_contacts mc
GROUP BY mc_prof
ORDER BY mc_prof;
```
