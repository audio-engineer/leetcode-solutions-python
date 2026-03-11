"""1. Two Sum.

https://leetcode.com/problems/two-sum/description/
"""

from typing import List

import pytest

from leetcode.two_sum_brute import Solution as BruteForceSolution
from leetcode.two_sum_hash import Solution as HashTableSolution


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum_brute(nums: List[int], target: int, expected: list[int]) -> None:
    assert expected == BruteForceSolution().twoSum(nums, target)


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum_hash(nums: List[int], target: int, expected: list[int]) -> None:
    assert expected == HashTableSolution().twoSum(nums, target)
