class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        if not heights:
            return 0
        stack = []
        for idx, val in enumerate(heights + [0]):
            while stack and val < heights[stack[-1]]:
                bar = stack.pop()
                height = heights[bar]
                width = (idx - stack[-1] - 1) if stack else idx
                max_area = max(max_area, height * width)
            stack.append(idx)
        return max_area
