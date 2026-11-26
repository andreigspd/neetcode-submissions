class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        current = n - 2
        while current >= 0:
            if current + nums[current] >= goal:
                goal = current
            current -= 1
        return goal == 0