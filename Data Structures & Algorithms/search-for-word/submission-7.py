class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        if not word:
            return True
        n = len(board)
        m = len(board[0])
        target = len(word)
        used = set()
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        found = False
        def dfs(i, j, k):
            nonlocal found
            if board[i][j] != word[k]:
                return
            used.add((i, j))
            if (k + 1) == target:
                found = True
                return
            for di, dj in dir:
                i_nou, j_nou = i + di, j + dj
                if (i_nou >= 0 and i_nou < n and j_nou >= 0 and j_nou < m) and (i_nou, j_nou) not in used:
                    dfs(i_nou, j_nou, k + 1)
            used.remove((i, j))
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    used.clear()
                    dfs(i, j, 0)
        return found
