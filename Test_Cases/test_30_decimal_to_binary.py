import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Codes" / "30_decimal_to_binary.py"
spec = importlib.util.spec_from_file_location("binary", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
decimal_to_binary = module.decimal_to_binary


def test_normal_number():
    assert decimal_to_binary(10) == "1010"


def test_zero():
    assert decimal_to_binary(0) == "0"


def test_one():
    assert decimal_to_binary(1) == "1"


def test_negative_number():
    try:
        decimal_to_binary(-5)
        assert False
    except ValueError:
        assert True


def test_large_number():
    assert decimal_to_binary(255) == "11111111"