class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(0, n):
            for j in range(0, m):
                    dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]