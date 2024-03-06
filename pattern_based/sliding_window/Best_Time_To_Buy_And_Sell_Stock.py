# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res


# Example 1
prices = [7, 1, 5, 3, 6, 4]
assert Solution().maxProfit(prices) == 5

# Example 2
prices = [7, 6, 4, 3, 1]
assert Solution().maxProfit(prices) == 0
