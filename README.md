[![python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=ffd343)](https://docs.python.org/3.12/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<!-- omit from toc -->
# Genetic Algorithm
A Python implementation of genetic algorithms.

Install this package using `pip`:

    pip install -e git+https://github.com/javidahmed64592/genetic-algorithm#egg=genetic_algorithm

To update the package:

    pip update -e git+https://github.com/javidahmed64592/genetic-algorithm#egg=genetic_algorithm

_Note: It is recommended to install this into a virtual environment._

<!-- omit from toc -->
## Table of Contents
- [uv](#uv)
- [Installing Dependencies](#installing-dependencies)
- [Using the Genetic Algorithm](#using-the-genetic-algorithm)
- [Testing, Linting, and Type Checking](#testing-linting-and-type-checking)
- [License](#license)

## uv
This repository is managed using the `uv` Python project manager: https://docs.astral.sh/uv/

To install `uv`:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh                                    # Linux/Mac
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" # Windows
```

## Installing Dependencies
Install the required dependencies using `pip`:

    uv sync

To install with `dev` dependencies:

    uv sync --extra dev

## Using the Genetic Algorithm
For an example of how to use the genetic algorithm, see `phrase_solver.ipynb` where it is used to generate a specific sentence from random characters.

## Testing, Linting, and Type Checking

- **Run tests:** `uv run pytest`
- **Lint code:** `uv run ruff check .`
- **Format code:** `uv run ruff format .`
- **Type check:** `uv run mypy .`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
