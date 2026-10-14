

import importlib.util
from pathlib import Path

file_path = (
    Path(__file__).parent.parent
    / "Codes"
    / "21_largest_word.py"
)

spec = importlib.util.spec_from_file_location(
    "largest_word_module", file_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

largest_word = module.largest_word


def test_normal_sentence():
    assert largest_word("I love programming") == "programming"


def test_first_word_is_longest():
    assert largest_word("programming is fun") == "programming"


def test_same_length_words():
    assert largest_word("cat dog sun") == "cat"


def test_empty_sentence():
    assert largest_word("") == ""


def test_single_word():
    assert largest_word("Python") == "Python"


def test_multiple_spaces():
    assert largest_word("I love   coding") == "coding"
