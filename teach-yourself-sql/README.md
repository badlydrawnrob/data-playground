# README

> Sam's Teach Yourself SQL in 10 minutes (4th edition)

I'll be adding a handful of examples that seem to be useful for my needs. Wherever
possible, leave it to the book as a resource (don't repeat yourself) and make sure you have it handy throughout your projects! Here's my goals:

1. Rapid prototyping[^1]
2. Customer analysis
3. Basic data (types, `json`, etc)
4. Interop with Ai offline models


## JUST F* DO IT!

> Just make a start, and learn on the way ...
> Take it from [Arnold](https://beusefulbook.com/). Be useful!

**Just start BUILDING!** Don't make the mistake of trying to deep dive, or run through ever single example before you start. That's the goal, the point, the purpose anyway. Make a start, see how it holds up, and iterate on the way.


## How to learn

1. Read the chapter
2. Execute the examples
3. Make notes (the best bits)
4. Condense the notes (lazy loading)
5. Make comments (avoid with obvious code)


## ⚠️ A little warning

> Trust no one!

1. Always backup![^2]
2. Be careful of malicious users![^3]
3. Keep your data under lock and key.
4. Never share customer data.
5. Pick the ONE way to do it (SQLite/Postgres).[^4]


## Useful links

1. The [book](https://forta.com/books/0672336073/)
2. The [data](https://forta.com/wp-content/uploads/books/0672336073/TeachYourselfSQL_SQLite.zip) (SQLite)
3. The [errata](https://forta.com/books/0672336073/errata/) (mistakes)
4. The [author's site](https://forta.com/) (code warning)[^5]


[^1]: This includes creating the database, normalisation, API design, etc, focusing on the most essential data and commands.

[^2]: Whenever you're making permanent changes, don't trust yourself, back up just to be safe. Exactly like you're doing with this repository!

[^3]: Validate and sanatize all data before it hits the database. Make sure your code doesn't allow [SQL injections](https://realpython.com/prevent-python-sql-injection/) from your API.

[^4]: If there's a shorthand, but it's not available in Postgres (or the other `db` you're highly likely to use) then use the "safe" and expanded version. Do the same wherever you can with methods _particular_ to only one `db`. In general I'll be using Postgres and SQLite (not MySQL) so focus on syntax for migration between those.

[^5]: For example, [some of this code](https://forta.com/books/0137653573/code/) is god-awful, but it's suitable for beginners _who are using the specifics of Python_ and we can do better. The "Captain Code" book has some fun examples, but we could either (a) take a subset of Python that we _really_ need (http servers) and introduce that, or lift the examples and refactor them with Elm (our go-to and deep dive language).