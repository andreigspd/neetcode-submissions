class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for idx, val in enumerate(temperatures):
            while stack and val > temperatures[stack[-1]]:
                lower_temp = stack.pop()
                answer[lower_temp] = idx - lower_temp
            stack.append(idx)
        return answer