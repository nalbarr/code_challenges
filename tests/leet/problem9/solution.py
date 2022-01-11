from leet.problem9 import solution as problem9


def test_positive_121(solution):
    is_palindrome = solution.isPalindrome(121)
    assert is_palindrome == True

def test_negative_121(solution):
    is_palindrome = solution.isPalindrome(-121)
    assert is_palindrome == False

def test_positive_10(solution):
    is_palindrome = solution.isPalindrome(10)
    assert is_palindrome == False

def main():
    solution = problem9.Solution(9, "Palindrome Number", "Easy")
    test_positive_121(solution)
    test_negative_121(solution)
    test_positive_10(solution)

if __name__ == "__main__":
    main()
