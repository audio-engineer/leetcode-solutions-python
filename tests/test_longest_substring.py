"""3. Longest Substring Without Repeating Characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""

import pytest

from leetcode.longest_substring import Solution


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("au", 2),
        ("aab", 2),
    ],
)
def test_length_of_longest_substring(s: str, expected: int) -> None:
    assert expected == Solution().lengthOfLongestSubstring(s)
