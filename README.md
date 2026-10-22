# shortlink

A tiny link shortener in three small packages, kept small on purpose: a showcase for
[diff social](https://diffsocial.dev), where each pull request opens as a room for people and agents.

| Package | Language | Does |
|---|---|---|
| [`ts/`](ts) | TypeScript | turns a page title into a short slug |
| [`rust/`](rust) | Rust | normalizes a link before it is shortened |
| [`py/`](py) | Python | writes the weekly clicks report |

Each runs its own tests in CI. Nothing here is meant for production.

## Running the tests

```sh
cd ts && npm ci && npm test
cd rust && cargo test
cd py && pip install -r requirements.txt && python -m unittest discover -s tests
```
