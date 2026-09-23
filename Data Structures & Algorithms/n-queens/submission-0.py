class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        x = [0] * n
        freq = [0] * n
        ans = []
        def ok(level):
            if level == 0:
                return True
            for i in range(level):
                if abs(level - i) == abs(x[level] - x[i]):
                    return False
            return True
        def bkt(level):
            if level == n:
                curr = []
                s = ""
                for i in range(n):
                    s = "." * x[i] + "Q" + "." * (n - x[i] - 1)
                    curr.append(s)
                ans.append(curr)
                return
            for i in range(n):
                if not freq[i]:
                    freq[i] = 1
                    x[level] = i
                    if ok(level):
                        bkt(level + 1)
                    freq[i] = 0
        bkt(0)
        return ans