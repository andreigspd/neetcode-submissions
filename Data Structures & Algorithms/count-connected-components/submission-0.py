class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        G = [[] for _ in range(n)]
        for x, y in edges:
            G[x].append(y)
            G[y].append(x)

        def dfs(node):
            visited[node] = 1
            for i in G[node]:
                if not visited[i]:
                    dfs(i)
    
        count = 0
        visited = [0] * n
        for node in range(n):
            if visited[node] == 0:
                dfs(node)
                count += 1
        return count