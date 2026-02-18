# README

> A fruits API using Python and the [Piccolo](https://piccolo-orm.com/) ecosystem!

This mocking example is based on Elm Land's [fruits API](https://github.com/elm-land/elm-land/tree/main/examples/06-query-parameters) to see the difference in speed and efficiency of Elm-based queries compared to SQLite and FastAPI.

## Versions

1. [Fruits API](https://tinyurl.com/fruits-api-0f2caad) with basic routes and no authentication
2. Fruits API with basic routes and authentication
3. Fruits API with query routes and authentication


## Conventions

1. Public `UUID` business identifier (auto-indexed)[^1]
2. Use Serial `ID`s (or bytes) when possible, both are faster than `String`!
3. JWT for authentication only, `/profile` endpoint for preferences[^2]
4. Piccolo already has a `BaseUser` and `BaseUser.login()` function
5. Piccolo Admin is potentially a security risk (use offline only?) 
6. Piccolo API and Admin don't need to be used, they're handy packages
7. Piccolo stores values as `Int` or `Text` with SQLite (even `json`)
8. Use `create_pydantic_models` sparingly and roll your own Pydantic types
9. Split API models from Data models wherever possible (not complected)
10. Avoid unecessary endpoints that could become a security risk


## Setup

> After running these commands, insert values into database.
> Add `Colors` first as it's a foreign key `Fruits.colors` (see `sqlite-utils.sql`).

We don't need to worry about user creation or hashing passwords, but currently we
set them up manually (rather than in-app). We can eventually build in `BaseUser.create_user()` when ready.

```bash
# Run the app (and create DB)
# Populate the database with `sqlite_utils.sql`
uv run main.py

# Setup the user table
piccolo migrations forwards user

# Create the user (see `bruno/collection.bru`
# for user details to use with CLI command)
piccolo user create

# Login and create JWT token (or use Bruno)
# `client_id` and `client_secret` not set!
curl -X 'POST' \
'http://localhost:8000/login' \
-H 'accept: application/json' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=password&username=[USER]&password=[PASSWORD]&scope=&client_id=none&client_secret=none'
```

## Coding style

> See the article `/words/coding-style` for my preferred style.

TL;DR: Zen, brutalist, minimal. Aim for statically typed functional where possible.


## To-Do list

> Handle all errors "just-in-time" but use logs and screenshots/123s so you can
> replicate the bug. Make sure to use logs and test the API with Bruno for correct
> and incorrect data.

1. Create a backup of the `dependencies=[Depends(transaction)]` method
2. Follow up the Bombardier and `timeout` theory (it's worse than default)
3. Fix naming conventions (and stick to them)
    - Singular -vs- plural (`Fruit`/`Fruits`, `/fruit`/`/fruits`, etc)
    - Capital or lowercase (`["list", "example"]`)
4. Bombardier and Locust tests
5. Can `BaseUser` be extended easily with a `UUID` field?
    - Seems awkward to do, maybe stick with `Serial` id.
6. Can I break the SQLite database with [bad types](https://github.com/piccolo-orm/piccolo/discussions/1247) (via the API)?
7. Check the "APIs you won't hate" book on standard return values
    - What [should be returned](https://softwareengineering.stackexchange.com/questions/314066/restful-api-should-i-be-returning-the-object-that-was-created-updated) from an update, delete, etc?


## Performance

> We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. Yet we should not pass up our opportunities in that critical 3%.

A counter quote is [design your systems well](http://www.joshbarczak.com/blog/?p=580), care about [web obesity](https://idlewords.com/talks/website_obesity.htm), [slow 4g](https://nordicapis.com/optimizing-apis-for-mobile-apps/), and take easy wins.

1. Prefer ATOMIC transactions (not bulk)
2. Never use a read/write when a write will do (`.returning()`)

**The big question in my mind is "Do you have customers yet?"** If the answer is "NO!" you can optimize all you like; it won't make a bit of difference. If you've got paying customers, understand bottlenecks before _strategic_ optimization.

See also [`building-with-fast-api`](https://github.com/badlydrawnrob/python-playground/tree/master/building-with-fast-api) for more details.


## Errors

> For a more comprehensive look at errors, see [`building-with-fast-api`](https://github.com/badlydrawnrob/python-playground/tree/master/building-with-fast-api)


## Potential improvements

1. Aim for beautiful, readable, ELi5 code
    - Code for your stupid future self!
2. Tesla 5 steps (less dumb spec, remove stuff, etc)
3. Minimise dependencies and don't make me think!
4. Finger painting for adults (learning frame)
    - Which features are we omitting? (beginner friendly)
    - What's your [readability](https://readable.com/) score?
5. Faster loading and performance (major bottlenecks)
    - If speed is negligible, easier to read takes precedence


## Storytelling

> How you sell your thing matters ... why should they care?

Evan Czaplicki's [talk](https://www.deconstructconf.com/2017/evan-czaplicki-on-storytelling) about communicating clearly your vision and why anybody should care (when perspectives differ). Quite useful for documentation, Quick Start guides, and writing in general. Piccolo is great, but there's areas in the writing (and onboarding) for improvement.


## Dependencies

> A big concern is having too many dependencies!

Just keep an eye on how fast these are changing and what impact it has on your maintenance.


## User experience

> See the "Van Man Problem" for API architecture and design.

1. `Delete` operations should always prompt the user to confirm.
2. Handle errors correctly. Don't leak sensitive information.
3. Authenticate all routes that require authentication, or are "risky".
    - Make sure it's the correct user that is allowed to edit their posts.
4. What data should be public? What data should be private?


## Security

> You're not Facebook. Or Google. Only build what you need.
> Make sure your `.config/git/ignore` file doesn't commit `*.sqlite` databases!

Backup your database **outside** of version control in production.

Aim for speed and ease of reading, but take care with security. I don't _really_ need a fully functioning JWT [with claims](https://github.com/piccolo-orm/piccolo/discussions/1277) like Auth0, only a secure way for a user to login and validate their routes. Only include a `UUID` in the `payload` (it's public anyway) and an expiry date. Anything else can be retrieved once logged in from a `/profile` endpoint and cached in `localStorage` if needed.

`HS256` is fine if you own the stack and aren't sharing the `SECRET` with anyone else. For working with 3rd party JWTs, you'll need to use a `RS256` public key, or supply that to a client you don't control (if you're supplying the JWT). The JWT should ideally be used as authoration/access only — not data storage (which could reveal personal information).

Some services use tokens as a method of avoiding database or other lookups, but that only matters at scale; for a small service hitting an extra `/profile` endpoint won't make a difference in speed. Some systems use it to provide permissions like scopes (see Auth0). Again, it's too early to worry about that stuff.

Build simply. Don't overplan. YAGNI!


## Models

> Currently I'm using `create_pydantic_models` and not _quite_ splitting API and DATA layer

Unless the API and DATA layer models need to vary, generating a single model that can be reused for `DataModelIn` and `DataModelOut` might work ok. FastAPI will check it for data integrity in `data: Request` and `response_model=`.


## 🐞 Bugs

For now, unless it's a blocking problem, just LOG it and move on. Find a workaround, unless it's essential to what you need to complete. You've raised a lot of issues.

### Pylance squiggles

Is this because `pyproject.toml` is `name="fruits"` and I also have a fruits subfolder?

### Naming conventions

> Have a naming convention and stick to it: singular or plural?

### 🤖 Ai fails hard

> Trying to understand `lifespan` and `contextlib` was a big fat fail!

- [Using LLMs](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) for coding
- Be extremely careful letting Ai handle critical parts of your app (human in the loop)

### Pydantic models for foreign keys

It seems [easier](https://github.com/piccolo-orm/piccolo/issues/1292) to just create your own flat-style Pydantic model!

### Pydantic `null` values

- [An issue here](https://github.com/piccolo-orm/piccolo/issues/1132)

## Piccolo documentation

- [Contributing](https://github.com/piccolo-orm/piccolo/issues/1274#issuecomment-3395426315) if you find any areas of improvement.




[^1]: Also an option is using _both_ `UUID` (or short uuid) _and_ a primary key (`Serial`) on which to do lookups and joins. The UUID would be public-facing and the primary key private. The downside is it may require an extra `select()` to grab the primary key.

[^2]: Some say that JWT [is a bad default](https://evertpot.com/jwt-is-a-bad-default/) but I'm going to use it anyway! We also don't currently have a `client_secret`.