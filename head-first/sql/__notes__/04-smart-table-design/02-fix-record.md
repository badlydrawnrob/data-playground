## Let's fix our record

> So, I need to find a clown who's <mark>name</mark> is Elsie, where was she <mark>last seen</mark>? What was she doing? What was her <mark>activity</mark> at the time?

Take our example record above. Write a description like the one above — ask yourself questions! Now, chunk the main points:

- Elsie is a clown with a `name`
- We want to know where she was `last_seen`
- We want to find out by searching her `activity`

It's far easier to answer "who's driving a `'little car'`?" in a query, if we made that chunk atomic:


```text
-[ RECORD 1 ]-------------------------------------
name       | Elsie
last_seen  | Cherry Hill Senior Center
appearance | F, red hair, green dress, huge feet
activities | little car
```

You can see we've changed `activities` to have one, and only one value, `'little car'`. We could have made `appearance` atomic too, but we don't need to query that column.

### But what if I want to make everything atomic?

If you wanted to go crazy and atomise _all_ the data, you'd have to do something like:

```text
-[ RECORD 1 ]-------------------------------------
name       | Elsie
last_seen  | Cherry Hill Senior Center
gender     | F
hair_color | red
clothing   | green dress  
other      | huge feet
activities | little car
```
