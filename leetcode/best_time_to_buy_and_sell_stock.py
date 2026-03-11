"""121. Best Time to Buy and Sell Stock.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maximum_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maximum_profit = max(maximum_profit, profit)
            else:
                left = right

            right += 1

        return maximum_profit
