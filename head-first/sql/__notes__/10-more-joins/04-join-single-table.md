## Join on a single table

```text
employee_id    Int     Primary Key
employee_name  String
manager_id     Int     Foreign key going back to the EmployeeId
```
```sql
SELECT t1.employee_name AS employee, t2.manager_name AS boss
FROM employees AS t1
INNER JOIN employees AS t2
ON t2.manager_id = t1.employee_id;
```


You can also join on the _same table_. One example is using a self-referencing foreign key:

- Self referencing foreign key:
    + primary key of table used within the same table for a different use case
    + you join the table _to itself_
- Simulates having two tables
- Reference one id on another
