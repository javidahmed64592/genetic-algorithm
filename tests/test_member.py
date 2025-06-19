"""Unit tests for the genetic_algorithm/member.py module."""

from genetic_algorithm.member import Member


class TestMember:
    """Unit tests for the Member class in the genetic_algorithm module."""

    def test_initialization(self, mock_member_low_fitness: Member) -> None:
        """Test that a Member is initialized with an empty chromosome."""
        assert mock_member_low_fitness.chromosome == "123"
        assert mock_member_low_fitness._new_chromosome == ""

    def test_fitness(self, mock_member_low_fitness: Member) -> None:
        """Test that the fitness of a Member is calculated correctly."""
        assert mock_member_low_fitness.fitness == len(mock_member_low_fitness.chromosome)

    def test_crossover(self, mock_member_low_fitness: Member, mock_member_high_fitness: Member) -> None:
        """Test the crossover method of the Member class."""
        child = Member()
        child.crossover(mock_member_low_fitness, mock_member_high_fitness, mutation_rate=0)

        # Stub implementation for crossover logic
        assert child._new_chromosome == mock_member_low_fitness.chromosome

    def test_apply_new_chromosome(self, mock_member_low_fitness: Member) -> None:
        """Test that the apply_new_chromosome method updates the chromosome correctly."""
        mock_member_low_fitness._new_chromosome = "new_chromosome"
        mock_member_low_fitness.apply_new_chromosome()
        assert mock_member_low_fitness.chromosome == "new_chromosome"

    def test_end_to_end(self, mock_member_low_fitness: Member, mock_member_high_fitness: Member) -> None:
        """Test the end-to-end process of crossover and applying a new chromosome."""
        child = Member()
        child.crossover(mock_member_low_fitness, mock_member_high_fitness, mutation_rate=0)
        child.apply_new_chromosome()
        assert child.chromosome == mock_member_low_fitness.chromosome
