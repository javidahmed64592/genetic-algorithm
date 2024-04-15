class TestPopulation:
    def test_given_three_members_when_checking_size_then_check_population_has_right_size(self, mock_population):
        assert len(mock_population._population) == 3

    def test_given_three_members_when_getting_best_member_then_check_correct_member_returned(
        self, mock_population, mock_member_high_fitness
    ):
        assert mock_population.best_member == mock_member_high_fitness
        assert mock_population.best_member.fitness == mock_population.best_fitness
        assert mock_population.best_member._chromosome == mock_population.best_chromosome

    def test_given_three_members_when_getting_random_member_then_check_member_in_population(self, mock_population):
        assert mock_population.random_member in mock_population._population
