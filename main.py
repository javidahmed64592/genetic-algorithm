import argparse
from typing import List

from src.ga import GeneticAlgorithm
from src.helpers import load_config, print_system_msg
from src.member import Member
from src.population import Population

CONFIG_FILE = "config/config.json"


class PhraseSolver(GeneticAlgorithm):
    """
    Simple application to use genetic algorithms to solve an alphanumeric phrase.
    """

    def __init__(self, mutation_rate: int) -> None:
        super().__init__(mutation_rate)
        self._phrase: str

    def __str__(self) -> str:
        _phrase_str = f"Population Phrase: {self._phrase}"
        return f"{super().__str__()}\n{_phrase_str}"

    @classmethod
    def create_and_run(
        cls, population_size: int, mutation_rate: int, phrase: str, mem_genes: List[str]
    ) -> GeneticAlgorithm:
        """ """
        _ga = cls(mutation_rate)
        _ga._phrase = phrase
        _ga._population = Population([Member(len(_ga._phrase), mem_genes) for _ in range(population_size)])
        print(_ga)
        _ga.run()
        return _ga

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
