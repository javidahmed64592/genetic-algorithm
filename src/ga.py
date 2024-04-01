import matplotlib.pyplot as plt
import numpy as np

from src.member import Member


class GeneticAlgorithm:
    """
    This class creates a population of members that will be trying to guess a
    provided phrase. The number of members in this population is determined by the
    population size. The members can select genes from the provided genes,
    and these genes in their chromosomes randomly mutate according to a
    specified mutation rate.
    """

    def __init__(self, population_size, phrase, mem_genes, mutation_rate=10):
        """
        Initialise a population of members of a specified size. The population uses
        a phrase for the members to calculate their fitness.

        Inputs:
        population_size: int, number of members for the population
        phrase: str, the phrase to be guessed by the members
        mem_genes: list, possible genes to be used by the members' chromosomes
        mutation_rate: int, probability for members' chromosomes to mutate
        """
        self.population = np.array([Member(len(phrase), mem_genes, mutation_rate) for _ in range(population_size)])
        self.population_size = population_size
        self.phrase = phrase
        self.mem_genes = mem_genes

        self.best_chromosome = ""
        self.max_fitness = 0
        self.population_fitness = np.empty(population_size)
        self.generation = 0

        self.max_fitness_history = []
        self.avg_fitness_history = []

    def __str__(self):
        """
        Return population size, phrase, and the possible genes.
        """
        return "Population Size: %s\nPopulation Phrase: %s\nMember Genes: %s" % (
            self.population_size,
            self.phrase,
            self.mem_genes,
        )

    def print_members(self):
        """
        Prints the chromosomes of each member in the population.
        """
        for index in range(self.population_size):
            print("Member %s Chromosome: %s" % (index + 1, self.population[index]))

    def print_avg_gens(self):
        """
        Prints the average number of generations required to guess the phrase if
        all guesses were random.
        """
        num_gens = (len(self.mem_genes) ** len(self.phrase)) / self.population_size
        print("If all guesses are random, it would take on average %s generations to guess the phrase." % num_gens)

    def calculate_population_fitness(self):
        """
        Calculates the fitnesses of each member in the population.
        """
        return np.array([member.calculate_fitness(self.phrase) for member in self.population])

    def evaluate(self):
        """
        Calculate the fitnesses of each member in the population and add the max
        and average fitness to lists.
        """
        # Calculate population fitness
        self.population_fitness = self.calculate_population_fitness()
        sorted = self.population[np.argsort(self.population_fitness)]

        # Find the member with the highest fitness
        best = sorted[-1]
        self.best_chromosome = best.chromosome
        self.max_fitness = best.fitness

        # Add fitness data to lists
        self.max_fitness_history.append(self.max_fitness)
        self.avg_fitness_history.append(np.average(self.population_fitness))

    def select_parent(self, parent):
        """
        Uses the Rejection Sampling technique to choose whether or not to use the
        provided parent for crossover.

        Inputs:
        parent: population_member, potential parent to use for crossover
        """
        if np.random.uniform(0, 1) < parent.fitness / self.max_fitness:
            return parent
        return None

    def evolve(self):
        """
        Crossover the chromosomes of the members and overwrite their existing
        chromosomes.
        """
        # Select parents for crossover
        for member in self.population:
            parentA = None
            parentB = None

            while parentA is None:
                parentA = self.select_parent(self.population[np.random.randint(self.population_size)])

            while parentB is None:
                potential_parent = self.population[np.random.randint(self.population_size)]
                if potential_parent != parentA:
                    parentB = self.select_parent(potential_parent)

            member.crossover(parentA, parentB)

        # Overwrite the chromosome with the new chromosome
        for member in self.population:
            member.apply_new_chromosome()

        # Increase generation
        self.generation += 1

    def run(self):
        """
        Run the evolution process.
        """
        self.generation = 1

        while True:
            # Evaluate the population
            gen = "Generation %s \t||" % self.generation
            self.evaluate()

            # Correct phrase found so break out of the loop
            if self.best_chromosome == self.phrase:
                print("%s Phrase solved to be: %s" % (gen, self.best_chromosome))
                break

            # Return the closest match and its associated fitness then evolve.
            print("%s Best Chromosome: %s \t|| Max Fitness: %s" % (gen, self.best_chromosome, self.max_fitness))
            self.evolve()

    def analyse(self):
        """
        Plot the max and average fitnesses for each generation.
        """
        plt.figure(figsize=(14, 8))

        x = np.arange(self.generation)
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
