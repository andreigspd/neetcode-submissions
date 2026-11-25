class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[src] = 0

        for _ in range(k + 1):
            temp_dist = dist[:]
            for u, v, cost in flights:
                if dist[u] != float("inf") and dist[u] + cost < temp_dist[v]:
                    temp_dist[v] = dist[u] + cost
            dist = temp_dist
        return dist[dst] if dist[dst] != float("inf") else -1
