class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        G = [[] for _ in range(n + 1)]
        for x, y, cost in times:
            G[x].append((y, cost))
        
        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        q = [(0, k)]

        while q:
            curr_dist, nod = heapq.heappop(q)
            if curr_dist > dist[nod]:
                continue
            for neighbour, d in G[nod]:
                new_dist = curr_dist + d
                if new_dist < dist[neighbour]:
                    dist[neighbour] = new_dist
                    heapq.heappush(q, (new_dist, neighbour))
        max_elem = max(dist[1:])
        return -1 if max_elem == float("inf") else max_elem
        