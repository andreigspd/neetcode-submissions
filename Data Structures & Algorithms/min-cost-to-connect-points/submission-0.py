class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        n = len(points)

        class DSU:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.rank = [0] * n
            
            def find(self, x):
                if x == self.parent[x]:
                    return x
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                rx = self.find(x)
                ry = self.find(y)
                if rx == ry:
                    return False
                if self.rank[rx] < self.rank[ry]:
                    self.parent[rx] = ry
                elif self.rank[rx] > self.rank[ry]:
                    self.parent[ry] = rx
                else:
                    self.parent[ry] = rx
                    self.rank[rx] += self.rank[ry]
                
                return True
            
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((i, j, dist))
        edges.sort(key = lambda x : x[2])

        dsu = DSU(n)
        
        msu_dist = 0
        msu = []

        for i, j, cost in edges:
            if dsu.union(i, j) != False:
                msu_dist += cost
                msu.append((i, j))
                if len(msu) == n - 1:
                    break
        return msu_dist




