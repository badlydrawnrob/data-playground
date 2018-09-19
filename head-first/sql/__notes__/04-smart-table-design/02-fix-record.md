## Let's fix our record

Take our example record above:

- Elsie is a clown with a `name`
- We want to know where she was `last_seen`
- We want to find out by searching her `activity`

It'd be far easier to search for who's driving a `'little car'` if we made that chunk atomic:


```text
-[ RECORD 1 ]-------------------------------------
name       | Elsie
last_seen  | Cherry Hill Senior Center
appearance | F, red hair, green dress, huge feet
activities | little car
```

You can see we've changed `activities` to have one, and only one value, `'little car'`. We could have made `appearance` atomic too, but we don't need to query that column.
