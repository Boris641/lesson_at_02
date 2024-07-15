import pytest
from Lesson_at_02 import count_vowels


@pytest.fixture
def test_cases():
    return [
        ("hello", 2),
        ("HELLO", 2),
        ("Привет", 2),
        ("ПРИВЕТ", 2),
        ("", 0),
        ("bcdfg", 0),
        ("aeiouаеёиоуыэюя", 15),
        ("AEIOUАЕЁИОУЫЭЮЯ", 15)
    ]

def test_count_vowels(test_cases):
    for s, expected in test_cases:
        result = count_vowels(s)
        assert result == expected, f"Expected {expected} for input '{s}', but got {result}"