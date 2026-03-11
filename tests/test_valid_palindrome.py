"""125. Valid Palindrome.

https://leetcode.com/problems/valid-palindrome/description/
"""

import pytest

from leetcode.valid_palindrome import Solution


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ],
)
def test_is_palindrome(s: str, expected: int) -> None:
    assert expected == Solution().isPalindrome(s)
