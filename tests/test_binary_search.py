"""704. Binary Search.

https://leetcode.com/problems/binary-search/description/
"""

from typing import List

import pytest

from leetcode.binary_search import Solution


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    ],
)
def test_check_inclusion(nums: List[int], target: int, expected: int) -> None:
    assert expected == Solution().search(nums, target)
