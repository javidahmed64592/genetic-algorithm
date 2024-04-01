import numpy as np


class Member:
    """
    This class creates a member of a population which has a chromosome of a
    specified length. The genes in the chromosome are chosen from the provided
    possible genes. The members can mix their chromosomes via crossover and
    there is a random chance for the genes to mutate during this process,
    controlled by the mutation rate.
    """

    def __init__(self, length, genes, mutation_rate=10):
        """
        Initialise a member for the population.

        Inputs:
          length: int, length of chromosome
          genes: list, all the possible genes
          mutation_rate: int, probability for a gene to randomly mutate
        """
        self.chromosome = ""
        self.new_chromosome = ""
        self.length = length
        self.genes = genes

        self.mutation_rate = mutation_rate
        self.fitness = 0

        self.generate_chromosome()

    def __str__(self):
        """
        Return the member's chromosome.
        """
        return self.chromosome

    def random_char(self):
        """
        Return a random gene from the possible genes.
        """
        return self.genes[np.random.randint(0, len(self.genes))]

    def generate_chromosome(self):
        """
        Generate a random sequence of genes for the chromosome.
        """
        self.chromosome = ""

        for _ in range(self.length):
            self.chromosome += self.random_char()

    def calculate_fitness(self, phrase):
        """
        Calculate the member's fitness based on the provided phrase.

        Inputs:
          phrase: str, used to compare chromosome to phrase and calculate fitness
        """
        self.fitness = 0
        score = 0

        for i in range(self.length):
            if self.chromosome[i] == phrase[i]:
                score += 1

        self.fitness = score**2
        return self.fitness

    def crossover(self, parentA, parentB):
        """
        Crossover the chromosomes of two parents to create a new chromosome.

        Inputs:
          parentA: population_member, used to construct new chromosome
          parentB: population_member, used to construct new chromosome
        """
        new_chromosome = ""

        for i in range(self.length):
            prob = np.random.randint(0, 100)

            # Half of the genes will come from parentA
            if prob < (100 - self.mutation_rate) / 2:
                new_char = parentA.chromosome[i]
            # Half of the genes will come from parentB
            elif prob < (100 - self.mutation_rate):
                new_char = parentB.chromosome[i]
            # Chance for a random genes to be selected
            else:
                new_char = self.random_char()

            new_chromosome += new_char

        self.new_chromosome = new_chromosome

    def apply_new_chromosome(self):
        """
        Overwrite the member's chromosome with the new chromosome from crossover.
        """
        self.chromosome = self.new_chromosome
