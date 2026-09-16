class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = set()
        for x in nums:
            if x in freq:
                return True
            freq.add(x)
        return False