"""Population class for genetic algorithm population."""

from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import NDArray

from genetic_algorithm.member import Member

rng = np.random.default_rng()


class Population:
    """Class for a population of members in a genetic algorithm.

    The population consists of a list of Member objects, each with a chromosome.
    The population can evaluate the fitness of its members and select parents for crossover.
    The best member can be retrieved based on fitness, and the population can select a random member.
    """

    def __init__(self, members: list[Member]) -> None:
        """Initialise Population with list of Members.

        :param list[Member] members:
            List of Member objects to create the population from.
        """
        self._members: NDArray = np.array(members)
        self._population_fitness: NDArray

    @property
    def size(self) -> int:
        """Return the size of the population."""
        return len(self._members)

    @property
    def random_member(self) -> Member:
        """Return a random member from the population."""
        _member: Member = rng.choice(self._members)
        return _member

    @property
    def best_member(self) -> Member:
        """Return the member with the highest fitness in the population."""
        _member: Member = self._members[np.argmax(self._population_fitness)]
        return _member

    @property
    def best_fitness(self) -> float:
        """Return the fitness of the best member in the population."""
        _fitness: float = np.max(self._population_fitness)
        return _fitness

    @property
    def best_chromosome(self) -> Any:  # noqa: ANN401
        """Return the chromosome of the best member in the population."""
        return self.best_member._chromosome

    @property
    def average_fitness(self) -> float:
        """Return the average fitness of the population."""
        _fitness: float = np.average(self._population_fitness)
        return _fitness

    def select_parent(self, other_parent: Member | None = None) -> Member:
        """Select a parent member from the population for crossover.

        :param Member other_parent:
            Parent to avoid selecting again for crossover. If None, any parent can be selected.
        :return Member:
            A randomly selected parent member from the population, avoiding the other_parent if provided.
        """
        while True:
            parent: Member = self.random_member
            if parent == other_parent:
                continue
            if rng.uniform(0, 1) < parent.fitness / self.best_fitness:
                return parent

    def evaluate(self) -> None:
        """Evaluate the population fitness and find best member."""
        self._population_fitness = np.array([member.fitness for member in self._members])
