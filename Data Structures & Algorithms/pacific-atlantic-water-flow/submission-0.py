class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        atl = [[0] * m for _ in range(n)]
        pac = [[0] * m for _ in range(n)]
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(i, j, path):
            path[i][j] = 1
            for di, dj in dir:
                i_nou, j_nou = i + di, j + dj
                if 0 <= i_nou < n and 0 <= j_nou < m and path[i_nou][j_nou] == 0 and heights[i_nou][j_nou] >= heights[i][j]:
                    dfs(i_nou, j_nou, path)

        for i in range(n):
            dfs(i, 0, pac)
            dfs(i, m - 1, atl)
        for i in range(m):
            dfs(0, i, pac)
            dfs(n - 1, i, atl)
        ans = []
        for i in range(n):
            for j in range(m):
                if atl[i][j] and pac[i][j]:
                    ans.append([i, j])
        return ans