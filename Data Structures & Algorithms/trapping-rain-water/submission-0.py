class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        water = 0
        max_left = 0
        max_right = 0
        while left < right:
            if heights[left] < heights[right]:
                if heights[left] >= max_left:
                    max_left = heights[left]
                else:
                    water += max_left - heights[left]
                left += 1
            else:
                if heights[right] >= max_right:
                    max_right = heights[right]
                else:
                    water += max_right - heights[right]
                right -= 1
        return water
        