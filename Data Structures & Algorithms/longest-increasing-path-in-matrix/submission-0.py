class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = {}
        max_lis = 0
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            lis = 1
            for di, dj in dir:
                nx, ny = i + di, j + dj
                if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] > matrix[i][j]:
                    lis = max(lis, 1 + dfs(nx, ny))
            dp[(i, j)] = lis
            return dp[(i, j)]


        for i in range(n):
            for j in range(m):
                if (i, j) not in dp:
                    dfs(i, j)
                max_lis = max(max_lis, dp[(i, j)])
        return max_lis
        