import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Codes" / "27_rotate_list.py"
spec = importlib.util.spec_from_file_location("rotation", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
rotate_list = module.rotate_list


def test_rotate_right():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_empty_list():
    assert rotate_list([], 3) == []


def test_large_k():
    assert rotate_list([1, 2, 3], 5) == [2, 3, 1]


def test_negative_k_rotates_left():
    assert rotate_list([1, 2, 3, 4], -1) == [2, 3, 4, 1]


def test_single_element():
    assert rotate_list([7], 10) == [7]