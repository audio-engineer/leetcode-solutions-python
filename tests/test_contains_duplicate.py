"""217. Contains Duplicate.

https://leetcode.com/problems/contains-duplicate/description/
"""

from typing import List

import pytest

from leetcode.contains_duplicate import Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ],
)
def test_contains_duplicate(nums: List[int], expected: bool) -> None:
    assert expected == Solution().containsDuplicate(nums)
