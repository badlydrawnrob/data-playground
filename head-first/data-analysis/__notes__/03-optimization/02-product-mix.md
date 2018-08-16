## Optimization charts

Which type of chart would you need to view an objective function that's aim is to optimise <b class="highlight highlight-underline">product mix</b> → <b class="highlight highlight-underline">profit</b>?

![Decision variable chart comparison]()

<b>Product mix 1 is good to go!</b> But, product mix 2 breaks our contraints.

> The bar chart is great if we only have one product line, or a single constraint, but what if we have more?

### A scatter plot chart is better

![Scatter plot chart example]()

If we plot our product mix on a chart like this, we can easily spot our "good to go", or _feasible_ region `:)`

Adding constraints to this chart will change the <b class="highlight highlight-underline">feasible region</b> and we can figure out what is the <b class="highlight highlight-underline">optimal value</b>

#### Changing the feasible region

What if we only had a certain amount of coffee beans to roast, grind and split between `☕ A` and `☕ B`?

![Diagram showing feasible regions of coffee cups]()

So, we can either make `500 * ☕ A` or `400 * ☕ B`, or split (mix) the coffee beans between them.

Because of these new constraints, we are even more limited in our <i>product mix</i> options. We can now use our ( C<sub><b>1</b></sub>D<sub><b>1</b></sub> ) + ( C<sub><b>2</b></sub>D<sub><b>2</b></sub> ) = P objective function to work out the `max(profit)`

![Image of A, B, C versions of product mix]()

```
A == ☹
B == 😌 ($5 * 100) + ($4 * 200)= $1300
C == 🤑 ($5 * 50) + ($4 * 300) = $1450
```

We can see that `C` brings the highest profit of the three.


## Optimisation is useless ...
### ... <i>unless</i> we make the right assumptions

In our previous models, we're picturing an ideal world where customers will buy whatever we make. This never happens! (or at least, it's incredibly rare).

😏 Customer assumptions. What will they buy?

> <b class="highlight highlight-bold"><em>All</em> models are wrong. But <em>some</em> are useful</b>! <i>[In other words, reality is complex — provide the closest, most useful model you can]</i> <cite>([George Box](https://en.wikipedia.org/wiki/All_models_are_wrong))</cite>

![IDEAL vs ACTUAL image]()

<b>Will the sky fall down?</b> Or might you just lose some cash? How closely your assumptions should mimic reality <i>depends on how important your results (or analysis) are</i>.

### Consider what assumptions you need to mimic reality

#### 1: What are the variables?

| Constraints | Decision variables |
|-------------|--------------------|
| 1. How long to produce | 1. How much of each to produce |
| 2. Cost of production | |
| 3. Profit | |

**... plus**

- real world constraints
- Buyer behaviour
- location

#### 2: What's the objective function?

> ( C<sub><b>1</b></sub>D<sub><b>1</b></sub> ) + ( C<sub><b>2</b></sub>D<sub><b>2</b></sub> ) **= P**

**... plus**

- C<sub><b>3</b></sub>: what sells?
- C<sub><b>4</b></sub>: in which store?
- C<sub><b>5</b></sub>: is there any industry data available?

#### 3: Ask yourself ...

1. What do you want to achieve?
2. What are the constraints?
    1. What's stopping you, or affecting you from getting it?
    2. <b class="highlight highlight-underline">List as many constraints</b> as possible, that you could represent quantatively with data!
