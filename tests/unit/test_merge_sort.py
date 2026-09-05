import pytest

from src.merge_sort import merge, merge_sort


@pytest.mark.unit
def test_merge_sort_empty_list():
    assert merge_sort([]) == []


@pytest.mark.unit
def test_merge_sort_single_element():
    assert merge_sort([10]) == [10]


@pytest.mark.unit
def test_merge_sort_descending_list():
    assert merge_sort([10, 8, 6, 4, 2, 0]) == [0, 2, 4, 6, 8, 10]


@pytest.mark.unit
def test_merge_two_sorted_lists():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
