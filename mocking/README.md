# README

> This can be used for any projects in other repositories.

For example:

- How To Elm: [`Films`](https://github.com/badlydrawnrob/elm-playground/blob/master/how-to-elm/src/CustomTypes/Films.elm) package.


## Questions

1. Consistency. Make decisions:
    - **`/` or `/new` for `POST` requests to create a thing**
    - `Fruit` or `Fruits` for table/model names (singular/plural)
    - `PUT` vs `PATCH` (I think go with explicit put requests)
    - Architecture routes and forms
2. Can I extract the singleton in a better way than `inserted[0]`?
3. Consider some form of GUI testing?
    - [Bruno testing](https://docs.usebruno.com/testing/tests/introduction)
4. Understand indexing a column and add it to your SQL notes (booklet)
    - 🔍 what does indexing a column do sqlite