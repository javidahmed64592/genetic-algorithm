[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=ffd343)](https://docs.python.org/3.11/)
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
- [Formatting, Type Checking and Linting](#formatting-type-checking-and-linting)

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

## Formatting, Type Checking and Linting
This library uses a number of tools for code formatting and linting. These tools are configured in `pyproject.toml`, `setup.cfg` and `mypy.ini`.

Black is used as a code formatter:

    black .

isort is used for tidying up imports:

    isort .

Mypy is used as a type checker:

    mypy .

Flake8 is used for linting:

    flake8
