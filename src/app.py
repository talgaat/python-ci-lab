def is_palindrome(s: str) -> bool:
    s2 = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s2 == s2[::-1]


def sum_numbers(nums):
    return sum(nums)
