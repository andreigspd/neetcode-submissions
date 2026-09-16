class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        car = [()] * n
        for i in range(n):
            car[i] = (position[i], speed[i])
        car.sort(reverse=True)
        stack = []
        for i in range(n):
            time = (target - car[i][0]) / car[i][1]
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack) 

