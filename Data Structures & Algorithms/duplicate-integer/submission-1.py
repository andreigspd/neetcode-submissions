class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return False
        
        seen_values = {}
        for x in nums:
            if x in seen_values:
                return True
            seen_values[x] = 1
        return False