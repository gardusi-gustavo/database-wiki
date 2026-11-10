# Data contract

`data/index.json` is the catalog. It contains `schema`, `generated_at`, and
`pages` with `id`, `title`, and `path`.

Each page lives under `data/pages/<slug>.json` and contains:

| Field | Type | Meaning |
| --- | --- | --- |
| `id` | string | Stable identifier |
| `title` | string | Display title |
| `slug` | string | URL-safe path segment |
| `tags` | array | Classification tags |
| `body` | string | Markdown body |
| `updated` | string | ISO date |

`dashboard-wiki` consumes this repository at build time and must not call it at
runtime.
