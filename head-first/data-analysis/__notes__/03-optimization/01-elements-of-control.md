## Elements of control

> When receiving a brief, it's helpful to collect data and group it by elements <em>you can control</em> and elements <em>you can't</em> - <strong>always</strong> ask for this data!

### Decision variables and constraints

> The balance of your _decision variables_ and your _constraints_ determine your profit

| **1:** Things you can control | **2:** Things you can't control |
|------------------------|--------------------------|
| _Your decision variables<br>.... **can** alter profit:_ | _Your constraints_<br>.... **can't** alter profit |
| — How much <i>Brand A</i> to buy | — Cost of each brand (wholesale) |
| — How much <i>Brand B</i> to buy | — How profitable each brand is |
| | — How much it costs to deliver |
| | — How long it takes to deliver |



### Optimization

> Example: if I increased production of (`☕ A`) or (`☕ B`), which would maximise profit?

You can maximise profit by choosing the right <i>product mix</i>. <b>Objective functions</b> help you decide how many of each product range (for example) to produce.

> An <mark>objective function</mark> is used when you want to find a `max()` or `min()` of something. This could be profit, or manpower, or logistics. You'll combine the things you <i>can</i> change with things you <i>can't</i> change to reach your objective.

#### An objective function

![!=Objective function or Latex]()

( C<sub><b>1</b></sub>D<sub><b>1</b></sub> ) + ( C<sub><b>2</b></sub>D<sub><b>2</b></sub> ) **= profit** (or the objective you want to achieve)

```
c = 'constraint'
d = 'decision variable'
```

Complex optimisations will need more sophisticated functions, but in essence, this is how an objective function looks.

![Cup A + Cup B = Total max(profit) sketch]()

The constraints in this case are profit for each coffee. The decision variable is how many of each to produce.

**Working it out ...**

```python
☕ = profit per cup
count = number of cups

(☕ A * count)  # total ☕ A profit
+
(☕ B * count)  # total ☕ B profit
=
profit
```

> This is for a very basic constraint: other variables, like time, materials etc will need further thought.
