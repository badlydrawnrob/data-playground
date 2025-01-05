## Finding the right product mix
### Optimization bar chart

We're trying to find the right <strong>product mix</strong> which will `max(profit)`. We could present our objective functions with a bar chart:

![Decision variable chart comparison]()

- <b>Product mix 1</b> is good to go!
- <s><b>Product mix 2</b> breaks our constraints</s>

Our bar chart is great if we only have one product line or a single constraint, but what if we have more? Which type of chart is will best present our objective functions?

### A scatter plot chart is better

![Scatter plot chart example]()

If we plot our product mix on a chart like this, we can easily spot our "good to go", or "feasible" region.

#### Changing the feasible region

Adding _constraints_ to this chart _changes the feasible region_ and we can figure out what is the <b class="highlight highlight-underline">optimal value</b>

- What if we only had a certain amount of coffee beans to roast and grind?
- These coffee beans must be split between `☕ A` and `☕ B`

![Diagram showing feasible regions of coffee cups]()

- We could make `500 * ☕ A` or `400 * ☕ B`
- Or, we could split (mix) the coffee beans between them

Because of these new constraints, we are even more limited in our product mix options. We can now use our [objective function](#anobjectivefunction) to work out the `max(profit)`

![Image of A, B, C versions of product mix]()

```python
A == ☹
B == 😌  # ($5 * 100) + ($4 * 200)= $1300
C == 🤑  # ($5 * 50) + ($4 * 300) = $1450
```

**Product mix `C`** brings the highest profit of the three!
