# algo

Algorithms and data structures practice project.

## Requirements

- Python 3.13+
- `uv` (recommended for environment and dependency management)
- `mise` (required for `mise run ...` task commands below)

## Setup

```bash
uv sync
```

This command creates/updates `.venv` and installs dependencies from `uv.lock`.

Install git hooks (recommended):

```bash
uv run pre-commit install
```

## Daily Commands

Run entry point:

```bash
uv run python main.py
```

Run CI-equivalent checks via custom commands (`mise`):

```bash
mise run ruff
mise run pylint
mise run mypy
mise run ci-local
```

Run pre-commit for all files:

```bash
uv run pre-commit run --all-files
```

Current pre-commit hooks run `ruff`, `mypy`, and `pylint` checks (plus whitespace/newline fixes).

## Migration from an existing `.venv`

If `.venv` was originally created with `python -m venv`, you can still migrate to `uv`:

1. Keep your existing project files.
2. Define dependencies in `pyproject.toml`.
3. Run `uv sync` to recreate/sync `.venv` from project metadata and `uv.lock`.

After migration, prefer `uv add`, `uv remove`, and `uv sync` for dependency operations.
