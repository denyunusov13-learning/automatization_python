import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("python", "Python"),
    ],
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "enter, result",
    [
        ("123abc", "123abc"),
        ("", ""),
        ("   ", "   "),
    ],
)
def test_capitalize_negative(enter, result):
    assert string_utils.capitalize(enter) == result


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),
        ("    hello world", "hello world"),
        (" python", "python"),
    ],
)
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("  ", ""),
        ("", ""),
        ("  123a", "123a"),
    ],
)
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, lit, expected",
    [
        ("skypro", "s", True),
        ("hello world", "l", True),
        ("python", "p", True),
    ],
)
def test_contains_positive(input_str, lit, expected):
    assert string_utils.contains(input_str, lit) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, lit, expected",
    [
        ("skypro", "a", False),
        ("hello world", "a", False),
        ("12345679", "8", False),
    ],
)
def test_contains_negative(input_str, lit, expected):
    assert string_utils.contains(input_str, lit) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, lit, expected",
    [
        ("Skypro", "S", "kypro"),
        ("hair", "r", "hai"),
        ("python", "pyth", "on"),
    ],
)
def test_delete_symbol_positive(input_str, lit, expected):
    assert string_utils.delete_symbol(input_str, lit) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, lit, expected",
    [
        ("", "s", ""),
        ("lamborgini", "zuuu", "lamborgini"),
        ("python", "", "python"),
        ("hello world", "l", "heo word"),
        ("chear", "chear", ""),
        ("Skypro", "s", "Skypro"),
    ],
)
def test_delete_symbol(input_str, lit, expected):
    assert string_utils.delete_symbol(input_str, lit) == expected
