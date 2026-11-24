class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        G = [[] for _ in range(n)]
        for x, y in edges:
            G[x].append(y)
            G[y].append(x)
        
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbour in G[node]:
                if neighbour == parent:
                    continue
                if neighbour in visited:
                    return False
                if dfs(neighbour, node) == False:
                    return False
            return True
        
        if dfs(0, -1) == False:
            return False
        for node in range(n):
            if node not in visited:
                return False
        return True
