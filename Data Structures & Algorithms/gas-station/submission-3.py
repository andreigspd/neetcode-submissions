class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = n - 1
        end = 0
        tank = gas[start] - cost[start]
        while start > end:
            if tank < 0:
                start -= 1
                tank += gas[start] - cost[start]
            else:
                tank += gas[end] - cost[end]
                end += 1

        if tank >= 0:
            return start
        return -1