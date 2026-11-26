class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for length in range(1, n - 1):
            for l in range(1, n - length):
                r = l + length - 1
                for i in range(l, r + 1):
                    coins = nums[l - 1] * nums[i] * nums[r + 1] + dp[l][i - 1] + dp[i + 1][r]
                    if coins > dp[l][r]:
                        dp[l][r] = coins
        return dp[1][n - 2]