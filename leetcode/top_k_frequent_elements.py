"""347. Top K Frequent Elements.

https://leetcode.com/problems/top-k-frequent-elements/description/
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies: dict[int, int] = {}

        for element in nums:
            if element not in frequencies:
                frequencies[element] = 1
            else:
                frequencies[element] += 1

        frequencies_sorted = sorted(
            frequencies.items(), key=lambda x: x[1], reverse=True
        )

        return [element for element, _ in frequencies_sorted[:k]]
