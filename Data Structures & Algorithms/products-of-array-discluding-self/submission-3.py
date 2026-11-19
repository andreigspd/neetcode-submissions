class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        prefix = 1
        ans = [1]
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            ans.append(prefix)
        postfix = 1
        for i in range(len(nums) - 2, -1, -1):
            postfix *= nums[i + 1]
            ans[i] *= postfix
        return ans