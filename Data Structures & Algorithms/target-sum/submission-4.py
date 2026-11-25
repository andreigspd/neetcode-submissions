class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        from collections import defaultdict

        dp = {0 : 1}
        for num in nums:
            new_dp = defaultdict(int)
            for current_sum, count in dp.items():
                new_dp[current_sum + num] += count
                new_dp[current_sum - num] += count
            dp = new_dp
        return dp[target]