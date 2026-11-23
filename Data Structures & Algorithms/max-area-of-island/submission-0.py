class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        self.area = 0
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j):
            grid[i][j] = 0
            self.area += 1
            for di, dj in dir:
                i_new, j_new = i + di, j + dj
                if (i_new >= 0 and i_new < n and j_new >= 0 and j_new < m) and grid[i_new][j_new] == 1:
                    dfs(i_new, j_new)
        

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.area = 0
                    dfs(i, j)
                    max_area = max(max_area, self.area)
        return max_area