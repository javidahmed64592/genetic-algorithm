import datetime

from src.ga import GeneticAlgorithm

if __name__ == "__main__":
    genes = list(
        "0123456789 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?"
    )  # Genes to be used by the members

    phrase = "I am a genetic algorithm!"  # Phrase to be guessed by the members
    mutation_rate = 2  # Percentage of genes in chromosomes to mutate
    population_size = 200  # Number of members in the population

    mypop = GeneticAlgorithm(population_size, phrase, genes, mutation_rate)
    print(mypop)
    mypop.print_avg_gens()

    begin_time = datetime.datetime.now()

    mypop.run()

    dt = datetime.datetime.now() - begin_time
    dt_m = int(dt.total_seconds() // 60)
    dt_s = int(dt.total_seconds() - (dt_m * 60))
    print("\n\nDone! The time it took is %sm %ss." % (dt_m, dt_s))

    mypop.analyse()
