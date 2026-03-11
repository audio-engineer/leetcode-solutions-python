"""1. Two Sum.

https://leetcode.com/problems/two-sum/description/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_i in enumerate(nums):
            sliced_nums = nums[i + 1 :]

            for j, num_j in enumerate(sliced_nums):
                if num_i + num_j == target:
                    return [i, len(nums) - len(sliced_nums) + j]

        return []
