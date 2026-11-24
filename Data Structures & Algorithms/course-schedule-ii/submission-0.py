class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = [[] for _ in range(numCourses)]
        deg = [0] * numCourses

        for x, y in prerequisites:
            G[x].append(y)
            deg[y] += 1
        
        from collections import deque
        q = deque()

        for node in range(numCourses):
            if deg[node] == 0:
                q.append(node)
        
        total = 0
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            total += 1
            for neighbour in G[node]:
                deg[neighbour] -= 1
                if deg[neighbour] == 0:
                    q.append(neighbour)
        if total < numCourses:
            return []
        return ans[::-1]