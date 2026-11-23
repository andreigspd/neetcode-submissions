class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def bfs(i, j):
            from collections import deque
            q = deque()
            q.append((i, j))
            vis = set()
            vis.add((i, j))
            edge = True if (i == 0 or i == n - 1 or j == 0 or j == m - 1) else False

            while q:
                x, y = q.popleft()
                for di, dj in dir:
                    nx, ny = x + di, y + dj
                    if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in vis and board[nx][ny] == "O":
                        q.append((nx, ny))
                        vis.add((nx, ny))
                        if (nx == 0 or nx == n - 1 or ny == 0 or ny == m - 1):
                            edge = True
            if edge == False:
                for x, y in vis:
                    board[x][y] = "X"

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    bfs(i, j)