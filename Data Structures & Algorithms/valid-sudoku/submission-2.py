class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or len(board) != 9 or len(board[0]) != 9:
            return False
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == ".":
                    continue
                sq = (i // 3) * 3 + (j // 3) % 3
                if ch in rows[i] or ch in cols[j] or ch in squares[sq]:
                    return False
                rows[i].add(ch)
                cols[j].add(ch)
                squares[sq].add(ch)
        return True