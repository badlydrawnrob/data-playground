## Confounders

> <b class="keywords keywords-highlight">Always</b> consider how <b class="keywords keywords-highlight">confounding</b> may <b class="keywords keywords-highlight">affect results</b>

- Confounders should make sense in the context of your analysis
- A confounder in one observational study, may not be relevant in another

Imagine you're conducting two studies. The economy is shot, consumer spending down, and your stores are in both _rich_ and _poor_ areas — sales are down and you're trying to find out why. For each theory, what are the confounders?

| ☕ Value perception | ☕ Temperature |
|---------------------|---------------|
| 📍 location | <s>📍 location</s> |
| -  | 👨🏻‍🍳 staff member   |
| -  | ⏰ time of day  |






## Managing Confounders

![Breaking the store survey results by region](./img/chunks-table.jpg)

> Break data into chunks

Sometimes it's a good idea to split out the data into smaller chunks, where the data is less likely to be biased. It'll help you manage confounders, some of which could be linked:

- 🔗 location
- 🔗 wealth
- age
- weather
- ...








## Are your observations valid?

> If I train staff better, will the temperature of the coffee improve?

- Sometimes a theory will overlap with observational data.
- Sometimes observations will give rise to a theory.
- Observational data is often unlikely to predict the future

### You'll need an experiment if

- Your observational data doesn't describe this theory
- There's not enough data to validate a theory, or give you predictions
- Your observational data isn't strong enough

If any of these are true, it's <strong>just a theory</strong>!





## Experimenting

![](./img/test-tubes.jpg)

> You might have two or more theories: <mark>You need an experiment!</mark>

You'd like to find out why people aren't buying.

1. Mark thinks it's a _pricing_ problem (discount, reduce price)
2. Ben thinks it's a _perception_ problem (rebrand)

Who's right?

### It's important to set a baseline

![Customer segment (theory and control) image]()

Let's take Mark's theory. If we went ahead and changed price across all stores, we can never be quite sure if our changes were the _real_ reason for failure or success!

- **Set a baseline control group**
    - An A/B test or experiment
    - A multivariate test
- **What would've happened _without_ the experiment?**
    - Did it have the desired effect?
    - Have you ruled out any confounders?

You can't <em>always</em> set a control, but always aim to.





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
