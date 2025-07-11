"""Genetic Algorithm implementation for evolving a population of members to guess a phrase."""

from __future__ import annotations

from genetic_algorithm.member import Member
from genetic_algorithm.population import Population


class GeneticAlgorithm:
    """Class for running a genetic algorithm on a population of members.

    The algorithm evaluates the population, analyses fitness, and evolves the members through crossover.
    Members can mutate during crossover based on a specified mutation rate.
    """

    def __init__(self, members: list[Member], mutation_rate: int) -> None:
        """Initialise a population of members of a specified size.

        :param list[Member] members:
            List of Members to create Population
        :param int mutation_rate:
            Probability for members' chromosomes to mutate
        """
        self._mutation_rate = mutation_rate
        self._population = Population(members=members)
        self._running = False
        self._generation = 1

    def __str__(self) -> str:
        """Return population size, phrase, and the possible genes."""
        _pop_str = f"Population Size: {self._population.size}"
        _mutation_str = f"Mutation Rate: {self._mutation_rate}"
        return f"{_pop_str}\n{_mutation_str}"

    def run(self) -> None:
        """Run the evolution process."""
        self._running = True
        self._generation = 1

        while self._running:
            self._evaluate()
            self._analyse()
            self._evolve()

    def _evaluate(self) -> None:
        """Evaluate the population."""
        self._population.evaluate()

    def _analyse(self) -> None:
        """Analyse population fitness."""
        _gen_text = f"Generation {self._generation:>4}:"
        _max_fitness_text = f"Max Fitness: {self._population.best_fitness}"
        _avg_fitness_text = f"Average Fitness: {self._population.average_fitness}"
        print(f"{_gen_text} \t{_max_fitness_text} \t{_avg_fitness_text}")

    def _evolve(self) -> None:
        """Crossover the chromosomes of the members and overwrite their existing chromosomes."""
        # Select parents for crossover
        for _member in self._population._members:
            _parent_a = self._population.select_parent()
            _parent_b = self._population.select_parent(_parent_a)
            _member.crossover(_parent_a, _parent_b, self._mutation_rate)

        # Overwrite the chromosome with the new chromosome
        for _member in self._population._members:
            _member.apply_new_chromosome()

        self._generation += 1
