class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if (s + target) % 2 == 1 or abs(target) > s:
            return 0
        subset_sum = (s + target) // 2

        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        for num in nums:
            for w in range(subset_sum, num - 1, -1):
                dp[w] += dp[w - num]
        return dp[subset_sum]
