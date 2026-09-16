class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            curr = nums[i]
            if (target - curr) in freq:
                return [freq[target - curr], i]
            freq[curr] = i
        return []