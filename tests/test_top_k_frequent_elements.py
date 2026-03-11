"""347. Top K Frequent Elements.

https://leetcode.com/problems/top-k-frequent-elements/description/
"""

from typing import List

import pytest

from leetcode.top_k_frequent_elements import Solution


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2, [1, 2]),
    ],
)
def test_two_sum_brute(nums: List[int], k: int, expected: list[int]) -> None:
    assert expected == Solution().topKFrequent(nums, k)
