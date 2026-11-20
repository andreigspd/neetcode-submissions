class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        water = 0
        n = len(heights)
        left_max = [1] * n
        right_max = [1] * n

        left_max[0] = heights[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], heights[i])
        right_max[n - 1] = heights[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], heights[i])
        
        for i in range(n):
            water += min(left_max[i], right_max[i]) - heights[i]
        return water