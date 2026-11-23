class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        if not grid:
            return None
        n = len(grid)
        m = len(grid[0])
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        INF = 2147483647

        def bfs():
            while q:
                pos = q.popleft()
                x, y = pos[0], pos[1]
                for di, dj in dir:
                    i_new, j_new = x + di, y + dj
                    if 0 <= i_new < n and 0 <= j_new < m and grid[i_new][j_new] == INF: 
                        q.append((i_new, j_new))
                        grid[i_new][j_new] = grid[x][y] + 1


        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))
        bfs()            
        