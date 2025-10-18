# README

> Some helpful info for a basic "fruits" api (similar to [Elm Land](https://github.com/elm-land/elm-land/tree/main/examples/06-query-parameters)'s version)

1. [`UUID`](https://github.com/piccolo-orm/piccolo/issues/1271) columns, or using short ids. Handle on [client side](https://dba.stackexchange.com/questions/307520/how-to-handle-short-uuids-with-postgres)?
2. [Authentication](https://github.com/piccolo-orm/piccolo/issues/1259) and using `Base.login()`
3. [`piccolo-api`](https://github.com/piccolo-orm/piccolo_api) is a [separate packge](https://github.com/piccolo-orm/piccolo/issues/1272) and SQLite DB drivers must be installed with Piccolo ORM package.
    - This should be more clearly labelled on the docs
    - You should also be able to easily `scaffold --fastapi`
    - You should also be able to `uv add 'piccolo-api[sqlite]'


## Dependencies

> A big concerns is having too many dependencies!

Just keep an eye on how fast these are changing and what impact it has on your maintenance.


## Bugs

> Have a naming convention and stick to it: singular or plural?

- Table `Fruit` or `Fruits`?
- Model `FruitModelIn` or `FruitsModelIn`?
- Folder `fruit` or `fruits`? (package)


## ORMs

> Piccolo seems to be one of the easiest ways to query data (see [ORM challenges](https://piccolo-orm.com/blog/orm-design-challenges/))

Peewee was great but not setup for async (it has an [untested plugin](https://peewee-async.readthedocs.io/en/latest/index.html)) and SQLModel is an abstraction of an abstraction (SQLAlchemy) which feels bloated. SQLModel does I think use the data mapper pattern rather than active record. It gets a bit confusing with `.session.exec()`, add, commit, etc, but isn't as object based as Peewee. Compared to both, however, Piccolo seems a lot lighter and easier to wrap your head around!


## User experience

> See the "Van Man Problem" for API architecture and design.

1. `Delete` operations should always prompt the user to confirm.
2. Handle errors correctly. Don't leak sensitive information.
3. Authenticate all routes that require authentication, or are "risky".
    - Make sure it's the correct user that is allowed to edit their posts.
4. What data should be public? What data should be private?
