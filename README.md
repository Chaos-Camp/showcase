# shortlink

A tiny link shortener in three small packages, kept small on purpose: it is a showcase for
[diff social](https://diffsocial.dev), where each pull request opens as a room.

| Package | Language | Does |
|---|---|---|
| [`ts/`](ts) | TypeScript | turns a page title into a short slug |
| [`rust/`](rust) | Rust | normalizes a link before it is shortened |
| [`py/`](py) | Python | writes the weekly clicks report |

Each runs its own tests in CI. Nothing here is meant for production.
