class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        freq = set()
        dir = [[1,0], [0, 1], [-1, 0], [0, -1]]
        n = len(board)
        m = len(board[0])
        def dfs(i, j, k):
            if k == len(word):
                return True
            board[i][j] = "#"
            for di, dj in dir:
                new_i = i + di
                new_j = j + dj
                if (new_i >= 0 and new_i < n and new_j >= 0 and new_j < m) and board[new_i][new_j] == word[k]:
                    if dfs(new_i, new_j, k + 1):
                        return True
            board[i][j] = word[k - 1]
            return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    freq.clear()
                    if dfs(i, j, 1):
                        return True
        return False
