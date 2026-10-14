import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "codes" / "22_anagram_strings.py"
spec = importlib.util.spec_from_file_location("anagram", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
is_anagram = module.is_anagram


def test_anagram():
    assert is_anagram("Listen", "Silent") is True


def test_case_and_spaces():
    assert is_anagram("Dormitory", "Dirty room") is True


def test_not_anagram():
    assert is_anagram("Hello", "World") is False


def test_empty_strings():
    assert is_anagram("", "") is True