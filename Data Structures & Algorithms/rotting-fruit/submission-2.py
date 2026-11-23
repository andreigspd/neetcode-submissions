class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        if not grid:
            return -1
        n = len(grid)
        m = len(grid[0])
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        dist = [[0] * m for _ in range(n)]

        q = deque()
        fruits = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fruits += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        min_time = 0

        if fruits == 0:
            return 0
        
        while q:
            x, y = q.popleft()
            for di, dj in dir:
                x_new, y_new = x + di, y + dj
                if 0 <= x_new < n and 0 <= y_new < m and grid[x_new][y_new] == 1 and dist[x_new][y_new] == 0:
                    fruits -= 1
                    q.append((x_new, y_new))
                    dist[x_new][y_new] = dist[x][y] + 1
                    min_time = max(min_time, dist[x_new][y_new])

        if fruits > 0:
            return -1
        return min_time
