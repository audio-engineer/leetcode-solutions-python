"""121. Best Time to Buy and Sell Stock.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""

from typing import List

import pytest

from leetcode.best_time_to_buy_and_sell_stock import Solution


@pytest.mark.parametrize(
    ("prices", "expected"),
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_max_profit(prices: List[int], expected: int) -> None:
    assert expected == Solution().maxProfit(prices)
