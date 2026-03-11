"""567. Permutation in String.

https://leetcode.com/problems/permutation-in-string/description/
"""

import pytest

from leetcode.permutation_in_string import Solution


@pytest.mark.parametrize(
    ("s1", "s2", "expected"),
    [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("adc", "dcda", True),
    ],
)
def test_check_inclusion(s1: str, s2: str, expected: bool) -> None:
    assert expected == Solution().checkInclusion(s1, s2)
