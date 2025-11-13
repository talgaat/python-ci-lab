import pytest
from src.palindrome import is_palindrome

def test_palindrome():
    assert is_palindrome("A man a plan a canal Panama") is True

def test_not_palindrome():
    assert is_palindrome("hello") is False

def test_empty():
    assert is_palindrome("") is True

def test_russian():
    assert is_palindrome("шалаш") is True