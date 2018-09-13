## Data and tables

![A computer with sticky notes on it](./img/sticky-notes.png)

Imagine a jumble of sticky notes. Each note has information about one of your friends; it might look like this:

```text
-----------------------
| Sticky note #1      |
| ------------------- |
| Name: Sam Dibb      |
| Address: Sunderland |
| Occupation: Sales   |
| Tel: 0191 5555 222  |
|                     |
=======================
```

It will fast become unorganised, and we can do better.

1. Look for **similar data types**, or patterns
2. Chunk your data into **categories**
3. What **label** might you give your _category_?
4. What **label** might you give your _sticky note_?

### Create a table

> A database contains tables; a table contains columns and rows.

Once we've chunked our data, it might look something like this:

```text
| database_name |

    | first_name | second_name | address    | occupation | telephone  |
    | ---------- | ----------- | ---------- | ---------- | ---------- |
    | Sam        | Dibb        | Sunderland | Sales      | 0191555222 |
    | ...        | ...         | ...        | ...        |            |
```

1. Your _categories_ become _column_ names
2. Your _friend_ becomes a _row_ in the table

#### Tables

- All tables in a database should be connected in some way

#### Columns

- A column describes the data with a label
- It should be descriptive and clearly explain the type of data
- Often referred to as _field_

#### Rows

- A row is a _set of columns_ that describe an _object_, or _thing_
- The columns can be thought of as an _objects attributes_
- Often referred to as _record_
