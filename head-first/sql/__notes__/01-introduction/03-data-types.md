## Data types

> It's important to make sure your _data chunk_ uses the correct _data type_

- There's lots of standard and fancy data types to choose from
- Each datatype has different _functions_ it's allowed to use
- You can add limitations and validation rules to each data type
- Check your types, they might be different in your <abbr title="relational database management system">RDBMS</abbr>
- See [postgres datatypes](#postgresdatatypes) for documentation

### Example datatypes

Using our `create table` example above, we could add the following data types to create our friends' table from our sticky note:

```sql
CREATE TABLE sticky_note (
  first_name VARCHAR(20),
  second_name VARCHAR(20),
  address VARCHAR(100)
  occupation VARCHAR(30)
  telephone INT(11)
)
```
