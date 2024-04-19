import pytest

from genetic_algorithm.member import Member
from genetic_algorithm.population import Population


@pytest.fixture
def mock_member_low_fitness() -> Member:
    _member = Member()
    _member._chromosome = "123"
    return _member


@pytest.fixture
def mock_member_med_fitness() -> Member:
    _member = Member()
    _member._chromosome = "1234"
    return _member


@pytest.fixture
def mock_member_high_fitness() -> Member:
    _member = Member()
    _member._chromosome = "12345"
    return _member


@pytest.fixture
def mock_population(
    mock_member_low_fitness: Member, mock_member_med_fitness: Member, mock_member_high_fitness: Member
) -> Population:
    pop = Population([mock_member_low_fitness, mock_member_med_fitness, mock_member_high_fitness])
    pop.evaluate()
    return pop
