import pytest

from src.list_generator import generate_list


@pytest.mark.unit
def test_generate_list_zero_size():
    assert generate_list(0) == []


@pytest.mark.unit
def test_generate_list_length():
    assert len(generate_list(10)) == 10


@pytest.mark.unit
def test_generate_list_values_are_int():
    result = generate_list(10)
    assert all(isinstance(value, int) for value in result)
