class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        n = len(nums)
        farthest = 0
        current_end = 0
        jumps = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                current_end = farthest
                jumps += 1
        return jumps