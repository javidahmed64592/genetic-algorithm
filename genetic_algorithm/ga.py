from __future__ import annotations

from typing import List

import numpy as np

from genetic_algorithm.member import Member
from genetic_algorithm.population import Population


class GeneticAlgorithm:
    """
    This class creates a population of members that will be trying to guess a
    provided phrase. The number of members in this population is determined by the
    population size. The members can select genes from the provided genes,
    and these genes in their chromosomes randomly mutate according to a
    specified mutation rate.
    """

    def __init__(self, mutation_rate: int) -> None:
        """
        Initialise a population of members of a specified size. The population uses a phrase for the members to
        calculate their fitness.

        Parameters:
            mutation_rate (int): Probability for members' chromosomes to mutate
        """
        self._mutation_rate = mutation_rate
        self._population: Population
        self._running = False
        self._generation = 1

    def __str__(self) -> str:
        """
        Return population size, phrase, and the possible genes.
        """
        _pop_str = f"Population Size: {self._population.size}"
        _mutation_str = f"Mutation Rate: {self._mutation_rate}"
        return f"{_pop_str}\n{_mutation_str}"

    def run(self) -> None:
        """
        Run the evolution process.
        """
        self._running = True
        self._generation = 1

        while self._running:
            self._evaluate()
            self._analyse()
            self._evolve()

    def _add_population(self, population: List[Member]) -> None:
        """
        Assign a List of Members to population.

        Parameters:
            population (List[Member]): List of Member objects to add
        """
        self._population = Population(members=population)

    def _evaluate(self) -> None:
        """
        Evaluate the population.
        """
        self._population.evaluate()

    def _analyse(self) -> None:
        """
        Analyse best member's chromosome.
        """
        _gen_text = f"Generation {self._generation:>4}:"
        _max_fitness_text = f"Max Fitness: {self._population.best_fitness}"
        print(f"{_gen_text} {self._population.best_chromosome} \t|| {_max_fitness_text}")

    def _evolve(self) -> None:
        """
        Crossover the chromosomes of the members and overwrite their existing chromosomes.
        """
        # Select parents for crossover
        for _member in self._population._population:
            _parentA = self._select_parent()
            _parentB = self._select_parent()
            _member.crossover(_parentA, _parentB, self._mutation_rate)

        # Overwrite the chromosome with the new chromosome
        for _member in self._population._population:
            _member.apply_new_chromosome()

        self._generation += 1

    def _select_parent(self) -> Member:
        """
        Uses the Rejection Sampling technique to choose whether or not to use a parent for crossover.

        Returns:
            parent (Member): Parent to use for crossover
        """
        while True:
            parent: Member = self._population.random_member
            if np.random.uniform(0, 1) < parent.fitness / self._population.best_fitness:
                return parent
