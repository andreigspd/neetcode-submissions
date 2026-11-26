class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        max_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1, n):
            max_sum = max(max_sum, curr_sum)
            curr_sum += nums[i]
            if curr_sum < nums[i]:
                curr_sum = nums[i]
        max_sum = max(max_sum, curr_sum)
        return max_sum