## Visualising probability words

> "What is the probability of `X`?" — "There's an `x`% chance of `x` happening"

Once you've completed your analysis of the key points, you can easily set up a table for all statements to be analysed. You can then plot these statement results on a graph:

| Analyst | Statement #1 | Statement #2 | ... |
|----|--------------|--------------|-----|
| 🤔 Tim |       %      | % | ... |
| 🤨 Bob | % | % | ... |

![Participants are scattered on the vertical, horizontal shows results](./img/statement-results.jpg)


## Are we in agreement?

| Results | 🤔 Tim | 🤨 Bob | ... | `stdev(range)` |
|----|--------------|--------------|-----|
| Statement #1 | % | % | ... | **%** |
| Statement #2 | % | % | ... | **%** |

![](./img/standard-deviation.jpg)

**Standard deviation** is a great way of answering "how close are the answers to each other?". It helps us view how far typical points are from the average.

1. **Smaller** standard deviation means **results are closer**
2. **Higher** standard deviation means **they disagree more**

### ⚠️ It's still subjective, remember!

This only _describes_ the data you're inputing — it's still subjective and will (probably) need to be iterated on with new data.
