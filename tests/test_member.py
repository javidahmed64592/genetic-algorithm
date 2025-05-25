from genetic_algorithm.member import Member


class TestMember:
    def test_member_initialization(self) -> None:
        member = Member()
        assert member.chromosome == ""
        assert member.fitness == 0

    def test_member_str(self) -> None:
        member = Member()
        member.chromosome = "test_chromosome"
        assert str(member) == "test_chromosome"

    def test_member_fitness(self) -> None:
        member = Member()
        member.chromosome = "test_chromosome"
        assert member.fitness == len(member.chromosome)

    def test_member_crossover(self) -> None:
        parent_a = Member()
        parent_b = Member()
        parent_a.chromosome = "AAAA"
        parent_b.chromosome = "BBBB"

        child = Member()
        child.crossover(parent_a, parent_b, mutation_rate=0)

        # Stub implementation for crossover logic
        assert child._new_chromosome == "AAAA"

    def test_member_apply_new_chromosome(self) -> None:
        member = Member()
        member._new_chromosome = "new_chromosome"
        member.apply_new_chromosome()
        assert member.chromosome == "new_chromosome"
