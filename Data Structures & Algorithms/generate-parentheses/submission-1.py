class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        ans = []
        def bkt(curr, open, closed):
            if closed > open:
                return
            if open > n:
                return
            if open == n and closed == n:
                ans.append("".join(curr))
            
            curr.append("(")
            bkt(curr, open + 1, closed)
            curr.pop()
            curr.append(")")
            bkt(curr, open, closed + 1)
            curr.pop()
        bkt([], 0, 0)
        return ans