import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Codes" / "29_armstrong_number.py"
spec = importlib.util.spec_from_file_location("armstrong", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
is_armstrong = module.is_armstrong


def test_armstrong_number():
    assert is_armstrong(153) is True


def test_not_armstrong():
    assert is_armstrong(123) is False


def test_negative_number():
    assert is_armstrong(-153) is False


def test_zero():
    assert is_armstrong(0) is True


def test_four_digit_armstrong():
    assert is_armstrong(9474) is True
    