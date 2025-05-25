from genetic_algorithm.member import Member
from genetic_algorithm.population import Population


class TestPopulation:
    def test_given_three_members_when_checking_size_then_check_population_has_right_size(
        self, mock_population: Population
    ) -> None:
        assert mock_population.size == len(mock_population._members)

    def test_given_three_members_when_getting_best_member_then_check_correct_member_returned(
        self, mock_population: Population, mock_member_high_fitness: Member
    ) -> None:
        assert mock_population.best_member == mock_member_high_fitness
        assert mock_population.best_member.fitness == mock_population.best_fitness
        assert mock_population.best_member._chromosome == mock_population.best_chromosome

    def test_given_three_members_when_getting_random_member_then_check_member_in_population(
        self, mock_population: Population
    ) -> None:
        assert mock_population.random_member in mock_population._members

    def test_given_parent_when_selecting_another_parent_then_check_different_parent_returned(
        self, mock_population: Population, mock_member_med_fitness: Member
    ) -> None:
        new_parent = mock_population.select_parent(mock_member_med_fitness)
        assert isinstance(new_parent, Member)
        assert new_parent != mock_member_med_fitness
