import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Codes" / "25_max_min_list.py"
spec = importlib.util.spec_from_file_location("maxmin", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
find_max_min = module.find_max_min


def test_normal_list():
    assert find_max_min([4, 9, 1, 7]) == (9, 1)


def test_single_element():
    assert find_max_min([5]) == (5, 5)


def test_negative_numbers():
    assert find_max_min([-8, -2, -10]) == (-2, -10)


def test_empty_list():
    try:
        find_max_min([])
        assert False
    except ValueError:
        assert True