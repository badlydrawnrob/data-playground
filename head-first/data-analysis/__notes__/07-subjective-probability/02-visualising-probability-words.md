## Visualising probability words

> "What is the probability of `X`?" — "There's an `x`% chance of `x` happening"

| 🤨 | Statement #1 | Statement #2 | ... |
|----|--------------|--------------|-----|
| #1 |       %      | % | ... |
| #2 | % | % | ... |

Once you've completed your analysis of the key points, you can easily set up a table for all statements to be analysed. You can then plot these statement results on a graph:

![Participants are scattered on the vertical, horizontal shows results](./img/statement-results.jpg)


## Are we in agreement?

| 🤨 | #1 | #2 | ... | `stdev(range)` |
|----|--------------|--------------|-----|
| Statement #1 | % | % | ... | **%** |
| Statement #2 | % | % | ... | **%** |

**Standard deviation** is a great way of answering "how close are the answers to each other?". It helps us view how far typical points are from the average.

![](./img/standard-deviation.jpg)

1. A smaller standard deviation means _results are closer_
2. A higher standard deviation means _they disagree more_

Again, this only _describes_ the data you're inputing ... it's still subjective and will (probably) need to be iterated on with new data.
