from __future__ import annotations

from typing import Any


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

    def __init__(self) -> None:
        """
        Initialise a Member for the population.
        """
        self._chromosome: Any
        self._new_chromosome: Any

    def __str__(self) -> str:
        """
        Return the member's chromosome.
        """
        return str(self._chromosome)

    @property
    def chromosome(self) -> Any:
        return self._chromosome

    @chromosome.setter
    def chromosome(self, new_chromosome: Any) -> None:
        self._chromosome = new_chromosome

    @property
    def fitness(self) -> int:
        """
        Return member fitness.
        """
        return len(self._chromosome)

    def crossover(self, parent_a: Member, parent_b: Member, mutation_rate: int) -> None:
        """
        Crossover the chromosomes of two parents to create a new chromosome.

        Parameters:
            parent_a (Member): Used to construct new chromosome
            parent_b (Member): Used to construct new chromosome
            mutation_rate (int): Probability for mutations to occur
        """
        self._new_chromosome = self._chromosome

    def apply_new_chromosome(self) -> None:
        """
        Overwrite the member's chromosome with the new chromosome from crossover.
        """
        self.chromosome = self._new_chromosome
