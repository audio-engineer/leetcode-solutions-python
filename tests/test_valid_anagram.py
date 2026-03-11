"""242. Valid Anagram.

https://leetcode.com/problems/valid-anagram/description/
"""

import pytest

from leetcode.valid_anagram import Solution


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "ab", False),
    ],
)
def test_is_anagram(s: str, t: str, expected: bool) -> None:
    assert expected == Solution().isAnagram(s, t)
