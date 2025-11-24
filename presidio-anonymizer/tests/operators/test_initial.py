import pytest

from presidio_anonymizer.operators import Initial

@pytest.mark.parametrize(
    "input_text, initials",
    [
        ("John Smith", "J. S."),
    ],
)
def test_given_value_for_initial(input_text, initials):
    text = Initial().operate(input_text) == initials
    assert text

def test_correct_name():
    assert Initial().operator_name() == "initial"

@pytest.mark.parametrize(
    "input_text, initials",
    [
        (" John Smith ", "J. S."),
    ],
)
def test_given_value_trims_whitespace(input_text, initials):
    text = Initial().operate(input_text) == initials
    assert text

@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("@abc", "@A."), #fulfills alphabetical scope
        ("@834A", "@8."), #fulfills numerical scope
        ("--**abc", "--**A.") #fulfills multiple preceeding characters
    ],
)
def test_initial_with_preceeding_special_characters(input_text, expected):
    result = Initial().operate(input_text)
    assert result == expected