class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for index, val in enumerate(heights + [0]):
            while stack and val < heights[stack[-1]]:
                mid = stack.pop()
                width = index - stack[-1] - 1 if stack else index
                height = heights[mid]
                area = height * width
                max_area = max(max_area, area)
            stack.append(index)
        return max_area
