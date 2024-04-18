[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=ffd343)](https://docs.python.org/3.11/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
<!-- omit from toc -->
# Genetic Algorithm
A Python implementation of genetic algorithms.

Install this package using `pipenv`:

```
pipenv install -e git+https://github.com/javidahmed64592/genetic-algorithm#egg=genetic_algorithm
```

<!-- omit from toc -->
## Table of Contents
- [Installing Dependencies](#installing-dependencies)
- [Using the Genetic Algorithm](#using-the-genetic-algorithm)
- [Testing](#testing)
- [Linting and Formatting](#linting-and-formatting)

## Installing Dependencies
Install the required dependencies using [pipenv](https://github.com/pypa/pipenv):

    pipenv install
    pipenv install --dev

## Using the Genetic Algorithm
For an example of how to use the genetic algorithm, see `phrase_solver.ipynb` where it is used to generate a specific sentence from random characters.

## Testing
This library uses Pytest for the unit tests.
These tests are located in the `tests` directory.
To run the tests:

    pipenv run test

## Linting and Formatting
This library uses `ruff` for linting and formatting.
This is configured in `ruff.toml`.

To check the code for linting errors:

    python -m ruff check .

To format the code:

    python -m ruff format .
