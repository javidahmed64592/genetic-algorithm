[![python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=ffd343)](https://docs.python.org/3.12/)
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
- [Installing Dependencies](#installing-dependencies)
- [Using the Genetic Algorithm](#using-the-genetic-algorithm)
- [Testing](#testing)
- [Linting and Formatting](#linting-and-formatting)
- [Type Checking](#type-checking)
- [License](#license)

## Installing Dependencies
Install the required dependencies using `pip`:

    pip install -e .

To install with `dev` dependencies:

    pip install -e .[dev]

## Using the Genetic Algorithm
For an example of how to use the genetic algorithm, see `phrase_solver.ipynb` where it is used to generate a specific sentence from random characters.

## Testing
This library uses Pytest for the unit tests.
These tests are located in the `tests` directory.
To run the tests:

    python -m pytest tests

## Linting and Formatting
This library uses `ruff` for linting and formatting.
This is configured in `pyproject.toml`.

To check the code for linting errors:

    python -m ruff check .

To format the code:

    python -m ruff format .

## Type Checking
This library uses `mypy` for static type checking.
This is configured in `pyproject.toml`.

To check the code for type check errors:

    python -m mypy .

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
