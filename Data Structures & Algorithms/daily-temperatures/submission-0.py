class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        results = [0] * n
        for index, val in enumerate(temperatures):
            while stack and val > temperatures[stack[-1]]:
                mid = stack.pop()
                results[mid] = index - mid
            stack.append(index)
        return results 