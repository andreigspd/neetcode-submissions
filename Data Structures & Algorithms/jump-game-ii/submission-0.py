class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if dp[j] != float("inf") and nums[j] >= i - j:
                    dp[i] = min(dp[i], 1 + dp[j])
        return dp[n - 1] 