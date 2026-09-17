class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy_price = prices[0]
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, prices[i] - buy_price)
            buy_price = min(buy_price, prices[i])
        return max_profit