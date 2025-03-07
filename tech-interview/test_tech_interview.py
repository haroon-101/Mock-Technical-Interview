import pytest
from tech_interview import palindrome_check, remove_punctuation, palindrome_check_list, get_word_from_dictionary


def test_palindrome_true():
    assert palindrome_check("racecar") == True


def test_palindrome_with_spaces():
    assert palindrome_check("race car") == False


def test_palindrome_false():
    assert palindrome_check("camel") == False


def test_palindrome_case():
    assert palindrome_check("Racecar") == True


def test_remove_punctuation():
    assert remove_punctuation("Hello!") == "Hello"


def test_palindrome_punctuation():
    text = "Racecar!"
    assert palindrome_check(remove_punctuation(text)) == True


def test_palindrome_list_success():
    words = ["oh", "hah", "yep", "mm"]
    assert palindrome_check_list(words) == ["hah", "mm"]


def test_palindrome_list_empty():
    words = ["oh", "yep"]
    assert palindrome_check_list(words) == []
