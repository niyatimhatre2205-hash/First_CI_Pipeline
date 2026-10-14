import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Codes" / "24_merge_sorted_lists.py"
spec = importlib.util.spec_from_file_location("merging", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
merge_sorted_lists = module.merge_sorted_lists


def test_normal_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_both_empty():
    assert merge_sorted_lists([], []) == []


def test_one_empty():
    assert merge_sorted_lists([], [1, 2]) == [1, 2]


def test_negative_numbers():
    assert merge_sorted_lists([-3, 0], [-2, 4]) == [-3, -2, 0, 4]
    