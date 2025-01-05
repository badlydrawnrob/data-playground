## LIKE statement

![When you want to find a value that looks _like_ something](./img/like.jpg)

You can search for a value `LIKE` another one. This comes in handy when:

- There might be typos or errors
- There might be many similar named values
- You might want to search _within_ text

### Wildcard rules

1. `%` stands for _any number of characters_
2. `_` stands for _one single character_


```sql
SELECT first_name FROM my_contacts
WHERE first_name LIKE '%nne';
```

Returns both `Anne` and `Roseanne` ...

```sql
SELECT first_name FROM my_contacts
WHERE first_name LIKE '_nne';
```

But this would only return `Anne`, or other words with a single character.
