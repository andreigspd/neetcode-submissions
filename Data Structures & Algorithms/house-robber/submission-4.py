class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        money = [0] * (n + 1)
        money[1] = nums[0]
        money[2] = max(nums[0], nums[1])
        for i in range(3, n + 1):
            money[i] = max(nums[i - 1] + money[i - 2], money[i - 1])
        return money[n]