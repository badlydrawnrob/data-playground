## 3NF

If changing any of the _non-key_ columns could cause any other columns to change, it's a transitive dependency. We're looking to avoid these!

1. Must be in 2NF
2. Has no transitive dependencies

```text
--[ courses ]--
course_id
course_name
instructor
instructor_phone
```

- We can ignore _primary key_ when considering 3NF
- No columns will change if we change a `course_name`
- `instructor` will not change if `instructor_phone` changes ...
- But `instructor_phone` will change if `instructor` does!

So it's obvious that `instructor_phone` belongs in the `instructor` table.
