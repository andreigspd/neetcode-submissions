class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) == 1:
            return [-1, -1]
        seen = {}
        #seen[i] = idx_i
        for idx, x in enumerate(nums):
            remaining = target - x
            if remaining in seen:
                return [seen[remaining], idx]
            seen[x] = idx
        return [-1, -1]
        