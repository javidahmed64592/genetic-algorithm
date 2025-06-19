"""Unit tests for the genetic_algorithm/population.py module."""

import numpy as np

from genetic_algorithm.member import Member
from genetic_algorithm.population import Population


class TestPopulation:
    """Unit tests for the Population class in the genetic_algorithm module."""

    def test_given_three_members_when_checking_size_then_check_population_has_right_size(
        self, mock_population: Population
    ) -> None:
        """Test that the population size is equal to the number of members."""
        assert mock_population.size == len(mock_population._members)

    def test_given_three_members_when_getting_best_member_then_check_correct_member_returned(
        self, mock_population: Population, mock_member_high_fitness: Member
    ) -> None:
        """Test that the best member is the one with the highest fitness."""
        assert mock_population.best_member == mock_member_high_fitness
        assert mock_population.best_member.fitness == mock_population.best_fitness
        assert mock_population.best_member._chromosome == mock_population.best_chromosome

    def test_given_three_members_when_getting_random_member_then_check_member_in_population(
        self, mock_population: Population
    ) -> None:
        """Test that a random member is selected from the population."""
        assert mock_population.random_member in mock_population._members

    def test_given_parent_when_selecting_another_parent_then_check_different_parent_returned(
        self, mock_population: Population, mock_member_med_fitness: Member
    ) -> None:
        """Test that a new parent is selected that is different from the given parent."""
        new_parent = mock_population.select_parent(mock_member_med_fitness)
        assert isinstance(new_parent, Member)
        assert new_parent != mock_member_med_fitness

    def test_given_population_when_evaluating_then_check_population_fitness_calculated(
        self, mock_population: Population
    ) -> None:
        """Test that the population fitness is calculated correctly."""
        expected_fitness = np.array([member.fitness for member in mock_population._members])
        assert np.array_equal(mock_population._population_fitness, expected_fitness)
        assert mock_population.best_fitness == max(mock_population._population_fitness)
        assert mock_population.average_fitness == sum(mock_population._population_fitness) / mock_population.size
