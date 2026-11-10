# database-wiki

Structured knowledge-base data for `dashboard-wiki`.

## Layout

| Path | Holds |
| --- | --- |
| `schemas/wiki.schema.json` | Page and index schema |
| `data/index.json` | Page catalog |
| `data/pages/` | Structured wiki pages |
| `docs/` | Data contract and usage notes |
| `docs/issues/` | Local task queue |

## Validation

```bash
bash infra/scripts/ci.sh
```

## Rules

- Public data only.
- Every page has a stable `id` and `slug`.
- Every index entry points to an existing page.
- No HTML or executable content in page bodies.
