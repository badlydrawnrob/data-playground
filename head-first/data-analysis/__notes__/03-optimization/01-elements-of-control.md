## Elements of control

> When receiving a brief, it's helpful to collect data and group it by elements <mark>you can control</mark> and elements <mark>you can't</mark> - <strong>always</strong> ask for this data!

### Decision variables and constraints

| **1:** Things you can control | **2:** Things you can't control |
|------------------------|--------------------------|
| How much <i>Brand A</i> to buy | Cost of each brand (wholesale) |
| How much <i>Brand B</i> to buy | How profitable each brand is |
| | How much it costs to deliver |
| | How long it takes to deliver |

1. These are your <b>decision variables</b>
    - These _can_ alter profit
2. These are your <b>constraints</b>
    - These _can't_ alter profit

> The balance of your decision variables and your constraints <mark>determine your profit</mark>


### Optimization

> Example: if I increased production of (`☕ A`) or (`☕ B`), which would maximise profit?

You can maximise profit by choosing the right <i>product mix</i>. <b>Objective functions</b> help you decide how many of each product range (for example) to produce.

> An <mark>objective function</mark> is used when you want to find a `max()` or `min()` of something. This could be profit, or manpower, or logistics. You'll combine the things you <i>can</i> change with things you <i>can't</i> change to reach your objective.

#### An objective function

![!=Objective function or Latex]()

( constraint<sub><b>1</b></sub> decision_variable<sub><b>1</b></sub> ) + ( constraint<sub><b>2</b></sub> decision_variable<sub><b>2</b></sub> )
**= Profit** (or the objective you want to achieve)

Complex optimisations will need more sophisticated functions, but in essence, this is how an objective function looks.

![Cup A + Cup B = Total max(profit) sketch]()

The constraints in this case are profit for each coffee. The decision variable is how many of each to produce.

##### Working it out ...

(profit per `☕ A` x count of cup) <small>_total `☕ A` profit_</small>
**+**
(profit per `☕ B` x count of cup) <small>_total `☕ B` profit_</small>
**= Profit**

> This is for a very basic constraint: other variables, like time, materials etc will need further thought.
