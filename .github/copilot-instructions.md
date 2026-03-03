# Copilot Instructions

## Repository Overview

This repository is a Python practice project for algorithms and data structures. Code is organized into chapters under the `components/` directory (e.g., `components/chap1/`, `components/chap2/`).

## Language & Runtime

- **Language**: Python 3
- **Runtime version**: managed via `mise` (see `mise.toml`) — use the latest Python version
- **Project metadata**: defined in `pyproject.toml`

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) conventions.
- All modules and public functions must have docstrings.
- Use type annotations where applicable.
- Linting is enforced with **pylint**. Ensure `pylint` passes before submitting changes:
  ```bash
  pip install pylint
  pylint $(git ls-files '*.py')
  ```

## Project Structure

```
components/
  chap1/   # Chapter 1 algorithms
  chap2/   # Chapter 2 algorithms
main.py    # Entry point
```

When adding a new algorithm or exercise, place it in the appropriate chapter directory under `components/`. Create a new chapter directory (e.g., `components/chap3/`) if the exercise belongs to a new chapter.

## CI

The repository uses a GitHub Actions workflow (`.github/workflows/pylint.yml`) that runs `pylint` on every push. Make sure all Python files pass pylint before pushing.
