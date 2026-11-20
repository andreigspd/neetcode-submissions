class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = float("inf")
        profit = 0
        for price in prices:
            if price < min_so_far:
                min_so_far = price
            else:
                profit = max(profit, price - min_so_far)
        return profit