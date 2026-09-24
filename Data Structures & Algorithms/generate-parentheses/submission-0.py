class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def bkt(open_p, closed_p, path):
            if open_p > n:
                return
            if closed_p > n:
                return
            if closed_p > open_p:
                return
            if open_p == n and closed_p == n:
                ans.append(path[:])
                return
            bkt(open_p + 1, closed_p, path + "(")
            bkt(open_p, closed_p + 1, path + ")")
        bkt(0, 0, "")
        return ans
