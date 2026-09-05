import pytest

from src.insertion_sort import insertion_sort


@pytest.mark.unit
def test_insertion_sort_empty_list():
    assert insertion_sort([]) == []


@pytest.mark.unit
def test_insertion_sort_single_element():
    assert insertion_sort([10]) == [10]


@pytest.mark.unit
def test_insertion_sort_descending_list():
    assert insertion_sort([10, 8, 6, 4, 2, 0]) == [0, 2, 4, 6, 8, 10]
