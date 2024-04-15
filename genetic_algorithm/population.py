from __future__ import annotations

from typing import Any, List

import numpy as np
from numpy.typing import NDArray

from genetic_algorithm.member import Member


class Population:
    """
    This class creates a population from a list of Member objects and has methods and properties for evaluating the
    population fitnesses.
    """

    def __init__(self, members: List[Member]) -> None:
        """
        Initialise Population with list of Members.

        Parameters:
            members (List[Member]): List of Member objects
        """
        self._population = np.array(members)
        self._population_fitness: NDArray

    def evaluate(self) -> None:
        """
        Evaluate the population fitness and find best member.
        """
        self._population_fitness = np.array([member.fitness for member in self._population])

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
