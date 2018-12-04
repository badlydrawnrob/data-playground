## UNION

![union illustration]()

...


```text
{'designer', 'dentist'} =>
{'nurse', 'designer'}   =>  {'designer', 'dentist', 'manager', 'nurse'}
{'manager'}             =>
```

You can even create a table from a `UNION`!

### Limitations

Each `SELECT` query must have:

- Same number of columns
- Same datatype


### UNION ALL

To show _every single_ record from each `SELECT`, *including* duplicates — use `UNION ALL`.
