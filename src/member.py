from __future__ import annotations

from typing import List

import numpy as np


class Member:
    """
    This class creates a member of a population which has a chromosome of a
    specified length. The genes in the chromosome are chosen from the provided
    possible genes. The members can mix their chromosomes via crossover and
    there is a random chance for the genes to mutate during this process,
    controlled by the mutation rate.

    Different simulations will have chromosomes of different types depending on
    the goal. Chromosome creation and crossover will need to be adjusted to suit
    the given task. The fitness function will also need to be changed.
    """

    def __init__(self, length: int, gene_pool: List[str], mutation_rate: int) -> None:
        """
        Initialise a member for the population.

        Parameters:
            length (int): Length of chromosome
            gene_pool (List[str]): List of possible genes
            mutation_rate (int): Probability for a gene to randomly mutate
        """
        self._length = length
        self._gene_pool = gene_pool
        self._mutation_rate = mutation_rate
        self._chromosome = ""
        self._new_chromosome = ""

    def __str__(self) -> str:
        """
        Return the member's chromosome.
        """
        return self.chromosome

    @property
    def chromosome(self) -> str:
        """
        Generate random chromosome if not already created and return.
        """
        if not self._chromosome:
            self._chromosome = "".join([self.random_char for _ in range(self._length)])
        return self._chromosome

    @property
    def random_char(self) -> str:
        """
        Return a random gene from the possible genes.
        """
        _choice: str = np.random.choice(self._gene_pool)
        return _choice

    @property
    def fitness(self) -> int:
        """
        Return member fitness.
        """
        return self._score**2

    def calculate_score(self, phrase: str) -> None:
        """
        Calculate the member's score based on the provided phrase.

        Parameters:
            phrase (str): Used to compare chromosome to phrase and calculate fitness
        """
        self._score = sum([self.chromosome[i] == phrase[i] for i in range(self._length)])

    def crossover(self, parent_a: Member, parent_b: Member) -> None:
        """
        Crossover the chromosomes of two parents to create a new chromosome.

        Parameters:
            parent_a (Member): Used to construct new chromosome
            parent_b (Member): Used to construct new chromosome
        """
        self._new_chromosome = ""

        for i in range(self._length):
            prob = np.random.randint(0, 100)

            # Half of the genes will come from parentA
            if prob < (100 - self._mutation_rate) / 2:
                new_char = parent_a.chromosome[i]
            # Half of the genes will come from parentB
            elif prob < (100 - self._mutation_rate):
                new_char = parent_b.chromosome[i]
            # Chance for a random genes to be selected
            else:
                new_char = self.random_char

            self._new_chromosome += new_char

    def apply_new_chromosome(self) -> None:
        """
        Overwrite the member's chromosome with the new chromosome from crossover.
        """
        self._chromosome = self._new_chromosome
