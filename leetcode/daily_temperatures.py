"""739. Daily Temperatures.

https://leetcode.com/problems/daily-temperatures/description/
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: list[int] = []
        result = [0] * len(temperatures)

        for i, _ in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()

                result[index] = i - index

            stack.append(i)

        return result
