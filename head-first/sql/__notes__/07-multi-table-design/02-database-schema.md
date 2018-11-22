## Database schema



### Atomic data (again)

Remember our atomic data rules?

- Only use the chunks you actually need
- Only break them down to the smallest chunk you'll need ...
    - _Don't_ use anything smaller just because you can
- Throw away anything you don't need

Well, our needs have outgrown our simple atomic data, so we'll need to change this:

```text
--[ Clown info ]--

id | attributes
---+-----------
1  | red hair, green dress, huge feet
```

Into a properly formatted table, further atomising `attributes` data into _rows_.


### What's a schema?

![](./img/database-schema.jpg)

A **schema** helps us understand the relationships between the data:

1. A description of the data (columns, tables)
2. How the objects relate to each other
3. How the columns and tables connect together
