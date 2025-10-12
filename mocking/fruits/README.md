# README

> Some helpful info for a basic "fruits" api (similar to [Elm Land](https://github.com/elm-land/elm-land/tree/main/examples/06-query-parameters)'s version)

1. Short UUIDs should be handled on the [client side](https://dba.stackexchange.com/questions/307520/how-to-handle-short-uuids-with-postgres)?


## ORMs

> Piccolo seems to be one of the easiest ways to query data (see [ORM challenges](https://piccolo-orm.com/blog/orm-design-challenges/))

Peewee was great but not setup for async (it has an [untested plugin](https://peewee-async.readthedocs.io/en/latest/index.html)) and SQLModel is an abstraction of an abstraction (SQLAlchemy) which feels bloated. SQLModel does I think use the data mapper pattern rather than active record. It gets a bit confusing with `.session.exec()`, add, commit, etc, but isn't as object based as Peewee. Compared to both, however, Piccolo seems a lot lighter and easier to wrap your head around!
