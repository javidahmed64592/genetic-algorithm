from src.ga import GeneticAlgorithm
from src.helpers import load_config

CONFIG_FILE = "config/config.json"


if __name__ == "__main__":
    ga_config = load_config(CONFIG_FILE)
    population_size = ga_config["population_size"]  # Number of members in the population
    mutation_rate = ga_config["mutation_rate"]  # Percentage of genes in chromosomes to mutate
    phrase = ga_config["phrase"]  # Phrase to be guessed by the members
    genes = list(ga_config["genes"])  # Genes to be used by the members

    mypop = GeneticAlgorithm(population_size, mutation_rate, phrase, genes)
    print(mypop)
    mypop.print_avg_gens()
    mypop.run()
    mypop.analyse()
