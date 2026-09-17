class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l, r = 0, 1
        dp = [0] * 2
        dp[0] = -prices[0]
        dp[1] = 0
        for i in range(1, n):
            dp[0] = max(dp[0], -prices[i])
            dp[1] = max(dp[1], dp[0] + prices[i])
        return dp[1]