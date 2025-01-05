## Optimization

> All optimization problems have constraints and an objective function

- **You can maximise profit** by choosing the right <i>product mix</i>
- **Objective functions** help you decide how many of each product range (for example) to produce.


### An objective function

![](./img/objective-function.jpg)

An _objective function_ is used when you want to find a `max()` or `min()` of something. This could be profit, manpower, or logistics. You'll combine the things you <i>can</i> change with things you <i>can't</i> change to reach your objective.

Complex optimisations will need more sophisticated functions, but in essence, this is how an objective function looks.

#### Example: objective function

> If I increased production of (`☕ A`) or (`☕ B`), which would maximise profit?

- The _constraints_ in this case are profit for each coffee.
- The _decision variable_ is how many of each to produce.

```python
a = $profit_per_☕ * number_of_☕  # total cup A profit
b = $profit_per_☕ * number_of_☕  # total cup B profit

a + b = profit
```


### ⚠️ It's rarely that simple!

Constraints are rarely this simple and will need further thought — the above example is a very basic constraint. Other variables might be:

- Time
- Materials
- Multiple products
- etc
