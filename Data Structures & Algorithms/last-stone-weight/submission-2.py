class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        q = []
        for stone in stones:
            heapq.heappush(q, -stone)
        while(len(q) > 1):
            y = heapq.heappop(q)
            x = heapq.heappop(q)
            if y == x:
                continue
            heapq.heappush(q, y - x)
        if len(q) == 0:
            return 0
        return -q[0]