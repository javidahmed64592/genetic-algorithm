from src.ga import GeneticAlgorithm

if __name__ == "__main__":
    genes = list(
        "0123456789 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?"
    )  # Genes to be used by the members

    phrase = "I am a genetic algorithm!"  # Phrase to be guessed by the members
    mutation_rate = 2  # Percentage of genes in chromosomes to mutate
    population_size = 200  # Number of members in the population

    mypop = GeneticAlgorithm(population_size, mutation_rate, phrase, genes)
    print(mypop)
    mypop.print_avg_gens()
    mypop.run()
    mypop.analyse()
