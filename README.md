# algo

Algorithms and data structures practice project.

## Requirements

- Python 3.13+
- `uv` (recommended for environment and dependency management)

## Setup

```bash
uv sync
```

This command creates/updates `.venv` and installs dependencies from `uv.lock`.

## Daily Commands

Run entry point:

```bash
uv run python main.py
```

Run lint/type checks:

```bash
uv run pylint $(git ls-files '*.py')
uv run mypy $(git ls-files '*.py')
```

## Migration from an existing `.venv`

If `.venv` was originally created with `python -m venv`, you can still migrate to `uv`:

1. Keep your existing project files.
2. Define dependencies in `pyproject.toml`.
3. Run `uv sync` to recreate/sync `.venv` from project metadata and `uv.lock`.

After migration, prefer `uv add`, `uv remove`, and `uv sync` for dependency operations.
