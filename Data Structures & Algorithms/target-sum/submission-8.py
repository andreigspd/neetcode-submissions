class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if (s + target) % 2 == 1 or abs(target) > s:
            return 0
        subset_sum = (s + target) // 2
        n = len(nums)
        dp = [[0] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for w in range(0, subset_sum + 1):
                dp[i][w] = dp[i - 1][w]
                if nums[i - 1] > w:
                    continue
                dp[i][w] += dp[i - 1][w - nums[i - 1]]
        return dp[n][subset_sum]