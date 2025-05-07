# README

> This is an example from OpenLibrary

- @ https://openlibrary.org/developers/api
- @ https://openlibrary.org/isbn/9780140328721.json
- @ https://covers.openlibrary.org/b/id/8739161-L.jpg
- @ https://covers.openlibrary.org/b/isbn/9780140328721-L.jpg

## Problems

> Until you can use a better API (like Nielsen Data), simplify your data.
> Consider only using the data points that are most consistent.

1. OpenLibrary isn't consistant: some fields don't appear for some books.
    - Do view this use [Json Diff](https://www.jsondiff.com/) tool with 2 books.
2. You'll probably need to strip slashes if searching for ISBN `978-0590353427`
3. Covers use a `[Int]` and not a `[String]`, but can still be accessed from ISBN number.