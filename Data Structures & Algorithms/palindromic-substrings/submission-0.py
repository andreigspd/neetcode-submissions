class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        count = 0
        dp = [[False] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i) <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1
        return count