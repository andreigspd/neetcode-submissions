class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        count = 0  
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j):
            grid[i][j] = str(-count)
            for di, dj in dir:
                i_new, j_new = i + di, j + dj
                if (i_new >= 0 and i_new < n and j_new >= 0 and j_new < m) and grid[i_new][j_new] == "1":
                    dfs(i_new, j_new)
        

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count