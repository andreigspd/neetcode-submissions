class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heapq.heapify_max(stones)
        while len(stones) > 1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            if y > x:
                heapq.heappush_max(stones, y - x)
        return stones[0] if stones else 0