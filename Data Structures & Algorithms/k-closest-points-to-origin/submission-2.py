class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        idx = 0
        for x, y in points:
            dist = (x ** 2 + y ** 2) ** (0.5)
            heapq.heappush_max(q, (dist, idx))
            idx += 1
            if len(q) > k:
                heapq.heappop_max(q)
        ans = []
        while q:
            dist, idx = heapq.heappop_max(q)
            ans.append(points[idx])
        return ans