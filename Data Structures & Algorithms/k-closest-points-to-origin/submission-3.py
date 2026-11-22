class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        q = []
        for point in points:
            x, y = point[0], point[1]
            dist = (x * x + y * y) ** (0.5)
            heapq.heappush(q, (-dist, x, y))
            if len(q) > k:
                heapq.heappop(q)
        ans = []
        while q:
            _, x, y = heapq.heappop(q)
            ans.append([x, y])
        return ans