"""11. Container With Most Water.

https://leetcode.com/problems/container-with-most-water/description/
"""

from typing import List

import pytest

from leetcode.container_with_most_water import Solution


@pytest.mark.parametrize(
    ("height", "expected"),
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], 15),
    ],
)
def test_max_area(height: List[int], expected: int) -> None:
    assert expected == Solution().maxArea(height)
