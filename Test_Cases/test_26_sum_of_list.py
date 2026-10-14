import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Codes" / "26_sum_of_list.py"
spec = importlib.util.spec_from_file_location("list_sum", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
sum_of_list = module.sum_of_list


def test_normal_list():
    assert sum_of_list([1, 2, 3, 4]) == 10


def test_empty_list():
    assert sum_of_list([]) == 0


def test_negative_numbers():
    assert sum_of_list([-1, -2, 3]) == 0


def test_single_element():
    assert sum_of_list([8]) == 8
