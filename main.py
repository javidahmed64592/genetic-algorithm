from __future__ import annotations

import argparse
from typing import List

import numpy as np

from src.ga import GeneticAlgorithm
from src.helpers import load_config, print_system_msg
from src.member import Member
from src.population import Population

CONFIG_FILE = "config/config.json"


class PhraseSolver(GeneticAlgorithm):
    """
    Simple app to use genetic algorithms to solve an alphanumeric phrase.
    """

    def __init__(self, mutation_rate: int) -> None:
        """
        Initialise PhraseSolver app.

        Parameters:
            mutation_rate (int)
        """
        super().__init__(mutation_rate)
        self._phrase: str

    def __str__(self) -> str:
        _phrase_str = f"Population Phrase: {self._phrase}"
        return f"{super().__str__()}\n{_phrase_str}"

    @classmethod
    def create_and_run(
        cls, population_size: int, mutation_rate: int, phrase: str, mem_genes: List[str]
    ) -> PhraseSolver:
        """
        Create app and run genetic algorithm.

        Parameters:
            population_size (int): Number of members in population
            mutation_rate (int): Mutation rate for members
            phrase (str): Phrase for members to solve
            mem_genes (List[str]): List of possible member genes

        Returns:
            ga (PhraseSolver): Phrase solver app
        """
        ga = cls(mutation_rate)
        ga._phrase = phrase
        ga._population = Population([PhraseSolverMember(len(ga._phrase), mem_genes) for _ in range(population_size)])
        print(ga)
        ga.run()
        return ga

    def _evaluate(self) -> None:
        """
        Evaluate the population.
        """
        self._population.calculate_member_scores(self._phrase)
        self._population.evaluate()

    def _analyse(self) -> None:
        """
        Analyse best member's chromosome.
        """
        _gen_text = f"Generation {self._generation:>4}:"

        # Correct phrase found so break out of the loop
        if self._population.best_chromosome == self._phrase:
            print_system_msg(f"{_gen_text} {self._population.best_chromosome} \t|| Solved!")
            self._running = False
            return

        # Return the closest match and its associated fitness then evolve.
        print_system_msg(
            f"{_gen_text} {self._population.best_chromosome} \t|| Max Fitness: {self._population.best_fitness}"
        )


class PhraseSolverMember(Member):
    """
    Member to use in PhraseSolver app.
    """

    def __init__(self, length: int, gene_pool: List[str]) -> None:
        """
        Initialise PhraseSolverMember with length of phrase and gene pool.

        Parameters:
            length (int): Length of member chromosome
            gene_pool (List[str]): List of possible characters
        """
        super().__init__()
        self._length = length
        self._gene_pool = gene_pool
        self._chromosome = "".join([self.random_char for _ in range(self._length)])

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
        self._score = sum([self._chromosome[i] == phrase[i] for i in range(self._length)])

    def crossover(self, parent_a: Member, parent_b: Member, mutation_rate: int) -> None:
        """
        Crossover the chromosomes of two parents to create a new chromosome.

        Parameters:
            parent_a (Member): Used to construct new chromosome
            parent_b (Member): Used to construct new chromosome
            mutation_rate (int): Probability for mutations to occur
        """
        self._new_chromosome = ""

        for i in range(self._length):
            prob = np.random.randint(0, 100)

            # Half of the genes will come from parentA
            if prob < (100 - mutation_rate) / 2:
                new_char = parent_a._chromosome[i]
            # Half of the genes will come from parentB
            elif prob < (100 - mutation_rate):
                new_char = parent_b._chromosome[i]
            # Chance for a random genes to be selected
            else:
                new_char = self.random_char

            self._new_chromosome += new_char


if __name__ == "__main__":
    ga_config = load_config(CONFIG_FILE)

    parser = argparse.ArgumentParser(description="Genetic Algorithm - Phrase Solver")
    parser.add_argument("--population_size", type=int, help="Number of members", default=ga_config["population_size"])
    parser.add_argument("--mutation_rate", type=int, help="Mutation rate", default=ga_config["mutation_rate"])
    parser.add_argument("--phrase", type=str, help="Phrase to solve", default=ga_config["phrase"])
    parser.add_argument("--gene_pool", type=str, help="Potential genes", default=ga_config["gene_pool"])
    args = parser.parse_args()

    population_size = args.population_size
    mutation_rate = args.mutation_rate
    phrase = args.phrase
    genes = list(args.gene_pool)

    ga = PhraseSolver.create_and_run(population_size, mutation_rate, phrase, genes)
