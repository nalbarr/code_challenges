import pytest

import leet
from leet.problem9 import solution as problem9


"""
9. Palindrome Number
- https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
- For example, 121 is a palindrome while 123 is not.

Example 1:
- Input: x = 121
- Output: true
- Explanation: 121 reads as 121 from left to right and from right to left.
"""
@pytest.fixture
def solution():
    solution = problem9.Solution(9, "Longest Palindrome", "Easy")
    return solution


def test_positive_121(solution):
    is_palindrome = solution.isPalindrome(121)
    assert is_palindrome == True


def test_negative_121(solution):
    is_palindrome = solution.isPalindrome(-121)
    assert is_palindrome == False


def test_positive_10(solution):
    is_palindrome = solution.isPalindrome(10)
    assert is_palindrome == False    
