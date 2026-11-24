class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        G = [[] for _ in range(numCourses)]
        deg = [0] * numCourses
        for x, y in prerequisites:
            G[x].append(y)
            deg[y] += 1
        total = 0
        q = deque()
        for node in range(numCourses):
            if deg[node] == 0:
                q.append(node)
                total += 1
        while q:
            node = q.popleft()
            for neighbour in G[node]:
                deg[neighbour] -= 1
                if deg[neighbour] == 0:
                    q.append(neighbour)
                    total += 1
        return total == numCourses