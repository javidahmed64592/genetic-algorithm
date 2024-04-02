import argparse

from src.ga import GeneticAlgorithm
from src.helpers import load_config

CONFIG_FILE = "config/config.json"


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

    mypop = GeneticAlgorithm(population_size, mutation_rate, phrase, genes)
    print(mypop)
    mypop.print_avg_gens()
    mypop.run()
    mypop.analyse()
