## Atomic data

![Make your data atomic for the best results!](./img/atomic.jpg)

The best database designs are **simple**, **specific**, and **fast**. In previous chapters, our table rows look something like this:

```text
-[ RECORD 1 ]-------------------------------------
name       | Elsie
last_seen  | Cherry Hill Senior Center
appearance | F, red hair, green dress, huge feet
activities | balloons, little car
```

- What happens if we want to search for records with `'red hair'`?
- What happens if we want to search for records driving a `little car`?

We could use `LIKE`, but it's better to make our data _atomic_.


### Break your data into smaller chunks

To make your data atomic, ask yourself the following questions:

1. What is **one** thing you want your table to describe?
2. What do you need to know about the thing? Make a list!
3. Break that down into the smallest chunks of data you need.
4. How might you label that data for your columns?
5. What type of data is it?

What's the focus? What's it's purpose? Think about the chunks of data you'll need:

1. Think about the chunks you'd need to use for your `SELECT` query
2. Think about the chunks you'd like to display as a result
3. Who's using or accessing the data?
4. What do they need? How will they search?


#### Only use what you need!

**Smaller is better!** Always build your tables in the easiest way possible, using only the information you'll need:

- Only use the chunks you actually need
- Only break them down to the smallest chunk you'll need ...
    - _Don't_ use anything smaller just because you can
- Throw away anything you don't need


#### What shall I name my atomic data?

- Use descriptive labels, like `last_seen`
- Make it short and easy to write (for your queries)

#### Atomic data rules

1. Each column must contain only one type of data
2. You can't have multiple columns with the same type of data
