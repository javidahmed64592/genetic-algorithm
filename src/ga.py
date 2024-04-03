from __future__ import annotations

from typing import List

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray

from src.helpers import print_system_msg
from src.member import Member


class GeneticAlgorithm:
    """
    This class creates a population of members that will be trying to guess a
    provided phrase. The number of members in this population is determined by the
    population size. The members can select genes from the provided genes,
    and these genes in their chromosomes randomly mutate according to a
    specified mutation rate.
    """

    def __init__(self, population_size: int, mutation_rate: int, phrase: str, mem_genes: List[str]) -> None:
        """
        Initialise a population of members of a specified size. The population uses a phrase for the members to
        calculate their fitness.

        Parameters:
            population_size (int): Number of members for the population
            mutation_rate (int): Probability for members' chromosomes to mutate
            phrase (str): The phrase to be guessed by the members
            mem_genes (List[str]): Possible genes to be used by the members' chromosomes
        """
        print_system_msg("Creating population...")
        self._population_size = population_size
        self._mutation_rate = mutation_rate
        self._phrase = phrase
        self._mem_genes = mem_genes

        self._population: NDArray = np.array([])
        self._max_fitness_history: List[int] = []
        self._avg_fitness_history: List[float] = []

    def __str__(self) -> str:
        """
        Return population size, phrase, and the possible genes.
        """
        _pop_str = f"Population Size: {self._population_size}"
        _mutation_str = f"Mutation Rate: {self._mutation_rate}"
        _phrase_str = f"Population Phrase: {self._phrase}"
        _genes_str = f"Member Genes: {self._mem_genes}"
        return f"{_pop_str}\n{_mutation_str}\n{_phrase_str}\n{_genes_str}"

    @property
    def population(self) -> NDArray:
        if not np.any(self._population):
            self._population = np.array(
                [Member(len(self._phrase), self._mem_genes) for _ in range(self._population_size)]
            )
        return self._population

    @classmethod
    def run_and_analyse(
        cls, population_size: int, mutation_rate: int, phrase: str, mem_genes: List[str]
    ) -> GeneticAlgorithm:
        _ga = cls(population_size, mutation_rate, phrase, mem_genes)
        print(_ga)
        _ga.print_avg_gens
        _ga.run()
        _ga.analyse
        return _ga

    def print_members(self) -> None:
        """
        Prints the chromosomes of each member in the population.
        """
        _mems_str = "\n".join(self.population)
        print_system_msg(f"Members:\n{_mems_str}")

    def print_avg_gens(self) -> None:
        """
        Prints the average number of generations required to guess the phrase if all guesses were random.
        """
        _num_gens = (len(self._mem_genes) ** len(self._phrase)) / self._population_size
        print_system_msg(
            f"If all guesses are random, it would take on average {_num_gens} generations to guess the phrase."
        )

    def run(self) -> None:
        """
        Run the evolution process.
        """
        print_system_msg("Running algorithm...")
        self._generation = 1

        while True:
            # Evaluate the population
            _gen = f"Generation {self._generation} \t||"
            self._evaluate()

            # Correct phrase found so break out of the loop
            if self._best_chromosome == self._phrase:
                print_system_msg(f"{_gen} Phrase solved to be: {self._best_chromosome}")
                break

            # Return the closest match and its associated fitness then evolve.
            print_system_msg(f"{_gen} Best Chromosome: {self._best_chromosome} \t|| Max Fitness: {self._max_fitness}")
            self._evolve()

            # Increase generation
            self._generation += 1

    def analyse(self) -> None:
        """
        Plot the max and average fitnesses for each generation.
        """
        print_system_msg("Generating plot...")
        plt.figure(figsize=(14, 8))

        x = np.arange(self._generation)
        normalisation = np.max(self._max_fitness_history)

        plt.plot(x, self._max_fitness_history / normalisation, label="Max Fitness", c="g")
        plt.plot(x, self._avg_fitness_history / normalisation, label="Avg Fitness")
        plt.title("Population Fitness vs Generation No.", fontsize=16)
        plt.xlabel("Generation no.", fontsize=16)
        plt.xlim([x[0], x[-1]])
        plt.xticks(fontsize=16)
        plt.ylabel("Fitness", fontsize=16)
        plt.ylim([0, 1])
        plt.yticks(fontsize=16)
        plt.legend(loc="best", fontsize=16)
        plt.show()

    def _calculate_population_fitness(self) -> NDArray:
        """
        Calculates the fitnesses of each member in the population.

        Returns:
            pop_fitness (NDArray): Array of fitnesses of each member
        """
        for _member in self.population:
            _member.calculate_score(self._phrase)
        pop_fitness = np.array([member.fitness for member in self.population])
        return pop_fitness

    def _select_parent(self) -> Member:
        """
        Uses the Rejection Sampling technique to choose whether or not to use a parent for crossover.

        Returns:
            parent (Member): Parent to use for crossover
        """
        while True:
            parent: Member = np.random.choice(self.population)
            if np.random.uniform(0, 1) < parent.fitness / self._max_fitness:
                return parent

    def _evaluate(self) -> None:
        """
        Calculate the fitnesses of each member in the population and add the max and average fitness to lists.
        """
        # Calculate population fitness
        _population_fitness = self._calculate_population_fitness()

        # Find the member with the highest fitness
        _best = self.population[np.argmax(_population_fitness)]
        self._best_chromosome = _best.chromosome
        self._max_fitness = _best.fitness

        # Add fitness data to lists
        self._max_fitness_history.append(self._max_fitness)
        self._avg_fitness_history.append(np.average(_population_fitness))

    def _evolve(self) -> None:
        """
        Crossover the chromosomes of the members and overwrite their existing chromosomes.
        """
        # Select parents for crossover
        for _member in self.population:
            _parentA = self._select_parent()
            _parentB = self._select_parent()
            _member.crossover(_parentA, _parentB, self._mutation_rate)

        # Overwrite the chromosome with the new chromosome
        for _member in self.population:
            _member.apply_new_chromosome()
