"""739. Daily Temperatures.

https://leetcode.com/problems/daily-temperatures/description/
"""

from typing import List

import pytest

from leetcode.daily_temperatures import Solution


@pytest.mark.parametrize(
    ("temperatures", "expected"),
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
    ],
)
def test_daily_temperatures(temperatures: List[int], expected: List[int]) -> None:
    assert expected == Solution().dailyTemperatures(temperatures)
