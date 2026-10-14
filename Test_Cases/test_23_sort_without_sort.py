import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Codes" / "23_sort_without_sort.py"
spec = importlib.util.spec_from_file_location("sorting", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
bubble_sort = module.bubble_sort


def test_normal_list():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_empty_list():
    assert bubble_sort([]) == []


def test_single_element():
    assert bubble_sort([7]) == [7]


def test_negative_numbers():
    assert bubble_sort([-3, 2, -1]) == [-3, -1, 2]


def test_original_list_unchanged():
    numbers = [3, 1, 2]
    bubble_sort(numbers)
    assert numbers == [3, 1, 2]
    