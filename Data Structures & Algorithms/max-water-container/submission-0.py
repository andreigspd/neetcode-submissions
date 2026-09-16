class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        max_height = 0
        while left < right:
            curr_height = min(heights[left], heights[right]) * (right - left)
            max_height = max(max_height, curr_height)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_height