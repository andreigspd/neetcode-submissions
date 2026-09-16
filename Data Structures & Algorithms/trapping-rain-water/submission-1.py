class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        water = 0
        for index, val in enumerate(heights):
            while stack and val > heights[stack[-1]]:
                mid = heights[stack.pop()]
                if stack:
                    left = heights[index]
                    right = heights[stack[-1]]
                    h = min(left, right) - mid
                    w = index - stack[-1] - 1
                    water += h * w
            stack.append(index)
        return water
        