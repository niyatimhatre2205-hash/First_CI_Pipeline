import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Codes" / "28_set_intersection.py"
spec = importlib.util.spec_from_file_location("intersection", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
set_intersection = module.set_intersection


def test_normal_sets():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_no_common_elements():
    assert set_intersection({1, 2}, {3, 4}) == set()


def test_empty_set():
    assert set_intersection(set(), {1, 2}) == set()


def test_negative_numbers():
    assert set_intersection({-1, 0, 2}, {-1, 3}) == {-1}
    