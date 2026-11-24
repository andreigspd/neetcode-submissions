class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
                rank[root_x] += rank[root_y]
            else:
                parent[root_x] = root_y
                rank[root_x] += rank[root_x]
            return True
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]