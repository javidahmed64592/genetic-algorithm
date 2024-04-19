from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import NDArray

from genetic_algorithm.member import Member


class Population:
    """
    This class creates a population from a list of Member objects and has methods and properties for evaluating the
    population fitnesses.
    """

    def __init__(self, members: list[Member]) -> None:
        """
        Initialise Population with list of Members.

        Parameters:
            members (list[Member]): List of Member objects
        """
        self._population = np.array(members)
        self._population_fitness: NDArray

    @property
    def size(self) -> int:
        return len(self._population)

    @property
    def random_member(self) -> Member:
        _member: Member = np.random.choice(self._population)
        return _member

    @property
    def best_member(self) -> Member:
        _member: Member = self._population[np.argmax(self._population_fitness)]
        return _member

    @property
    def best_fitness(self) -> float:
        _fitness: float = np.max(self._population_fitness)
        return _fitness

    @property
    def best_chromosome(self) -> Any:
        return self.best_member._chromosome

    @property
    def average_fitness(self) -> float:
        _fitness: float = np.average(self._population_fitness)
        return _fitness

    def select_parent(self, other_parent: Member | None = None) -> Member:
        """
        Uses the Rejection Sampling technique to choose whether or not to use a parent for crossover.

        Parameters:
            other_parent (Member | None): Other parent to ensure Member does not have two of the same parent

        Returns:
            parent (Member): Parent to use for crossover
        """
        while True:
            parent: Member = self.random_member
            if parent == other_parent:
                continue
            if np.random.uniform(0, 1) < parent.fitness / self.best_fitness:
                return parent

    def evaluate(self) -> None:
        """
        Evaluate the population fitness and find best member.
        """
        self._population_fitness = np.array([member.fitness for member in self._population])
