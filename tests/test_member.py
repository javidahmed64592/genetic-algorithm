from genetic_algorithm.member import Member


class TestMember:
    def test_initialization(self, mock_member_low_fitness: Member) -> None:
        assert mock_member_low_fitness.chromosome == "123"
        assert mock_member_low_fitness._new_chromosome == ""

    def test_fitness(self, mock_member_low_fitness: Member) -> None:
        assert mock_member_low_fitness.fitness == len(mock_member_low_fitness.chromosome)

    def test_crossover(self, mock_member_low_fitness: Member, mock_member_high_fitness: Member) -> None:
        child = Member()
        child.crossover(mock_member_low_fitness, mock_member_high_fitness, mutation_rate=0)

        # Stub implementation for crossover logic
        assert child._new_chromosome == mock_member_low_fitness.chromosome

    def test_apply_new_chromosome(self, mock_member_low_fitness: Member) -> None:
        mock_member_low_fitness._new_chromosome = "new_chromosome"
        mock_member_low_fitness.apply_new_chromosome()
        assert mock_member_low_fitness.chromosome == "new_chromosome"

    def test_end_to_end(self, mock_member_low_fitness: Member, mock_member_high_fitness: Member) -> None:
        child = Member()
        child.crossover(mock_member_low_fitness, mock_member_high_fitness, mutation_rate=0)
        child.apply_new_chromosome()
        assert child.chromosome == mock_member_low_fitness.chromosome
