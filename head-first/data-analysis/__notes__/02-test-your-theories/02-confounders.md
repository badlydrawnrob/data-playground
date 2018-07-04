## Confounders

> <b class="keywords keywords-highlight">Always</b> consider how <b class="keywords keywords-highlight">confounding</b> may <b class="keywords keywords-highlight">affect results</b>

- [ ] Confounders should make sense in the context of your analysis

![Confounders sketch]()

Manage confounders by breaking the data into chunks. Sometimes it's a good idea to split out the data into smaller chunks, where the data is less likely to be biased.

Some good examples are: location, wealth, age, weather, etc — sometimes these may be linked! (wealthy locations)

![pg.50 splitting the tables]()

> 🙄 Sometimes a theory will overlap with observational data. Or, sometimes observations will give rise to a theory.

- [x] If the observational data doesn't describe this theory, you'll need an experiment.
    - [ ] e.g if there's not enough (or good enough) data to validate a theory, or give you predictions — it's <strong>just a theory</strong>!
    - <q>If I train staff better, will the temperature of the coffee improve?</q>
- [ ] Observational data will often <em>not</em> be able to predict the future





## Experimenting

> You might have two or more theories: <mark>You need an experiment!</mark>

![3 test tubes image]()

> <mark>Always set a baseline</mark>

![Customer segment (theory and control) image]()

- [x] Always set a baseline control group
    - [ ] An A/B test or experiment
    - [ ] You need to know <i>what would have happened</i> without the experiment!
    - [ ] You can't <em>always</em> set a control, but always aim to.





## Randomise

When you randomise, the factors that might otherwise become confounders get equal representation in control/experiment groups.

> **pg.64—67** <mark>!= NEEDS EXPANDING / ILLUSTRATION / example</mark>

```text
I think it means — if age was a confounder — split into separate age groups and test control groups within these micro-groups
```

> <mark>Random</mark> selection gets you as close as possible to <mark>causal relationships</mark>

### An example confounder ...

Here's a group of people we want to test an experiment on:

![Image of confounder bug]()

The experiment groups should be random. This equals out any potential <i>confounders</i>, as each should contain them in equal amounts. They are essentially the same, other than the variable you're testing for.

![Image of random experiment]()

- [x] This is the case, <b>even if you don't know what the confounder is!</b>
    - [ ] Ideally you'd equal out everything _except_ the variable you're testing for, but that's best case scenario.

1. First try to avoid any obvious confounders, like location
    - [ ] See Starbuzz example [**pg: 67** grouping by micro-regions]
2. Next, <b>randomly assign</b> those groups to the <b>control</b> and <b>experiment</b>

> 💡 This is an example of a <mark>randomised controlled experiment</mark>
