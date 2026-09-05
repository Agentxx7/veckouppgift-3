import pytest

from src.insertion_sort import insertion_sort
from src.list_generator import generate_list


@pytest.mark.performance
@pytest.mark.parametrize("size", [500, 1000, 2000, 3000, 4000, 8000])
def test_insertion_sort_performance(benchmark, size):
    test_data = generate_list(size)

    result = benchmark(insertion_sort, test_data)

    assert result == sorted(test_data)
