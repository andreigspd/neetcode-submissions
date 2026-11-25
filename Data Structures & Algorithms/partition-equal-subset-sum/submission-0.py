class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]
        return dp[n][target]
            