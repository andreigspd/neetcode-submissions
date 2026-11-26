class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [float("-inf")] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + nums[i]
            if dp[i] < nums[i]:
                dp[i] = nums[i]
        return max(dp)
