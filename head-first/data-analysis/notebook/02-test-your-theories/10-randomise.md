## Randomise

> Random selection gets you as close as possible to causal relationships

We've already tried:

- Chunking the regions
- Running an A/B experiment

**Confounders may still plague our experiments!** In order to reduce our confounders _our groups need to be the same_. We could try the following:

1. <s>Charge every other customer a different price</s> (wouldn't go down well)
2. <s>Historical controls (has historical confounders)</s>
3. <s>Randomly assign stores control and experiment groups</s> (customers may choose cheapest)
4. Divide big geographic regions into micro regions (and randomly assign to control/experiment)

When you randomise, the factors that might otherwise become confounders get equal representation in control/experiment groups. So if we had a hidden confounder "X", both groups should contain the hidden confounder in (roughly) equal amounts. It _should_ (but not guaranteed to) affect your groups in equal ways.

![Randomise your experimental groups to minimise confounders](./img/randomise.jpg)

So, here were the steps we took:

1. First try to avoid any obvious confounders, like location
    - See Starbuzz example [**pg: 67** grouping by micro-regions]
2. Next, <b>randomly assign</b> those groups to the <b>control</b> and <b>experiment</b>
    - Ideally you'd equal out everything _except_ the variable you're testing for, but that's best case scenario.

### ⚠️ Other confounders to consider

- Sample size
- [Observer or subject bias](http://www.biostathandbook.com/confounding.html)
