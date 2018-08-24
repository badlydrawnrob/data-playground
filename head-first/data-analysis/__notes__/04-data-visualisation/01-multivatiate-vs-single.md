## Multivatiate -vs- single

### Scatterplots

A scatterplot explores <i class="highlight highlight-italic">causes</i>. It's an example of <i class="highlight highlight-italic">exploratory data analysis</i> (having a peak at the data that needs testing).

When creating a scatterplot, you're asking two main questions:

1. What is your objective or goal?
2. What are the expected causes for this goal to move <abbr title="up">↑</abbr> or <abbr title="up">↓</abbr>?

You then look at two variables together: the thing you're testing (potential "cause", or `x`); the goal or objective (`y`):

```
x = 'independent variable'
y = 'dependent variable'
```

![](./img/x-causes-y.jpg)

- Does one variable affect another?
- Does one variable affect the objective, or goal?

### An example scatterplot

![The circles are the intersection between `x` and `y`](./img/time-on-site.jpg)

> **Example:** objective = $revenue

Here we can see our `😀 customer` spent:

1. `x = 10` minutes on the site
2. `y = 40` dollars worth of stuff

### Comparing multiple variables

> You don't have to prove it! All you're looking for is <i class="highlight highlight-bold">patterns</i> and <i class="highlight highlight-bold">cause/effects</i>.

A single visualisation compares the relationship between _two variables_. When looking at variables in data analysis, _more is better_ — looking at charts together is a way of testing multivariate variables:

![](./img/multivariate.jpg)

Look around at data visualisations, including the authority on the subject, Edward Tufte. How good a job are they doing?

- How many variables do they have?
    - If there are <i class="highlight highlight-italic">3 or more</i> variables, they're more likely to be making intelligent comparisons and summaries.
- Is it _data art_ or _data analysis_?
    - It isn't data analysis if you can't directly understand the underlying data from the visuals.
