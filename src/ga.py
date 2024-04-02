from typing import List

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray

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
        Initialise a population of members of a specified size. The population uses
        a phrase for the members to calculate their fitness.

        Parameters:
        population_size (int): Number of members for the population
        mutation_rate (int): Probability for members' chromosomes to mutate
        phrase (str): The phrase to be guessed by the members
        mem_genes (List[str]): Possible genes to be used by the members' chromosomes
        """
        self._population_size = population_size
        self._mutation_rate = mutation_rate
        self._phrase = phrase
        self._mem_genes = mem_genes

        self._population: List[Member] = []
        self.max_fitness_history: List[int] = []
        self.avg_fitness_history: List[float] = []

    def __str__(self) -> str:
        """
        Return population size, phrase, and the possible genes.
        """
        _pop_str = f"Population Size: {self._population_size}"
        _phrase_str = f"Population Phrase: {self._phrase}"
        _genes_str = f"Member Genes: {self._mem_genes}"
        return f"{_pop_str}\n{_phrase_str}\n{_genes_str}"

    @property
    def population(self) -> List[Member]:
        if not np.any(self._population):
            self._population = np.array(  # TODO: Make not array?
                [Member(len(self._phrase), self._mem_genes) for _ in range(self._population_size)]
            )
        return self._population

    def print_members(self) -> None:
        """
        Prints the chromosomes of each member in the population.
        """
        _mems_str = "\n".join(self.population)
        print(_mems_str)

    def print_avg_gens(self) -> None:
        """
        Prints the average number of generations required to guess the phrase if
        all guesses were random.
        """
        num_gens = (len(self._mem_genes) ** len(self._phrase)) / self._population_size
        print("If all guesses are random, it would take on average %s generations to guess the phrase." % num_gens)

    def calculate_population_fitness(self) -> NDArray:
        """
        Calculates the fitnesses of each member in the population.
        """
        for member in self.population:
            member.calculate_score(self._phrase)
        return np.array([member.fitness for member in self.population])

    def evaluate(self) -> None:
        """
        Calculate the fitnesses of each member in the population and add the max
        and average fitness to lists.
        """
        # Calculate population fitness
        _population_fitness = self.calculate_population_fitness()
        sorted = self.population[np.argsort(_population_fitness)]

        # Find the member with the highest fitness
        best = sorted[-1]
        self.best_chromosome = best.chromosome
        self.max_fitness = best.fitness

        # Add fitness data to lists
        self.max_fitness_history.append(self.max_fitness)
        self.avg_fitness_history.append(np.average(_population_fitness))

    def select_parent(self, parent: Member) -> Member | None:
        """
        Uses the Rejection Sampling technique to choose whether or not to use the
        provided parent for crossover.

        Inputs:
        parent (Member): Potential parent to use for crossover
        """
        if np.random.uniform(0, 1) < parent.fitness / self.max_fitness:
            return parent
        return None

    def evolve(self) -> None:
        """
        Crossover the chromosomes of the members and overwrite their existing
        chromosomes.
        """
        # Select parents for crossover
        for member in self.population:
            parentA = None
            parentB = None

            while parentA is None:
                parentA = self.select_parent(np.random.choice(self.population))

            while parentB is None:
                potential_parent = np.random.choice(self.population)
                if potential_parent != parentA:
                    parentB = self.select_parent(potential_parent)

            member.crossover(parentA, parentB, self._mutation_rate)

        # Overwrite the chromosome with the new chromosome
        for member in self.population:
            member.apply_new_chromosome()

    def run(self) -> None:
        """
        Run the evolution process.
        """
        self._generation = 1

        while True:
            # Evaluate the population
            gen = "Generation %s \t||" % self._generation
            self.evaluate()

            # Correct phrase found so break out of the loop
            if self.best_chromosome == self._phrase:
                print("%s Phrase solved to be: %s" % (gen, self.best_chromosome))
                break

            # Return the closest match and its associated fitness then evolve.
            print("%s Best Chromosome: %s \t|| Max Fitness: %s" % (gen, self.best_chromosome, self.max_fitness))
            self.evolve()

            # Increase generation
            self._generation += 1

    def analyse(self) -> None:
        """
        Plot the max and average fitnesses for each generation.
        """
        plt.figure(figsize=(14, 8))

        x = np.arange(self._generation)
        normalisation = np.max(self.max_fitness_history)

        plt.plot(x, self.max_fitness_history / normalisation, label="Max Fitness", c="g")
        plt.plot(x, self.avg_fitness_history / normalisation, label="Avg Fitness")
        plt.title("Population Fitness vs Generation No.", fontsize=16)
        plt.xlabel("Generation no.", fontsize=16)
        plt.xlim([x[0], x[-1]])
        plt.xticks(fontsize=16)
        plt.ylabel("Fitness", fontsize=16)
        plt.ylim([0, 1])
        plt.yticks(fontsize=16)
        plt.legend(loc="best", fontsize=16)
        plt.show()
