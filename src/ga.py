from __future__ import annotations

import numpy as np

from src.helpers import print_system_msg
from src.member import Member
from src.population import Population


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
        print_system_msg("Creating population...")
        self._mutation_rate = mutation_rate
        self._population: Population
        self._running = False

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
        print_system_msg("Running algorithm...")
        self._running = True
        self._generation = 1

        while self._running:
            self._evaluate()
            self._analyse()
            self._evolve()
            self._generation += 1

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
        print_system_msg(f"{_gen_text} {self._population.best_chromosome} \t|| {_max_fitness_text}")

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
