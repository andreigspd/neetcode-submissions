class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) <= 1:
            return 0
        left = 0
        right = len(heights) - 1
        most_water = 0
        while left < right:
            current_water = min(heights[left], heights[right]) * (right - left)
            most_water = max(most_water, current_water)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return most_water