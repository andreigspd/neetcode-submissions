class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        start = 0
        max_len = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i ) <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if (j - i + 1) > max_len:
                        start = i
                        max_len = j - i + 1
        return s[start : start + max_len]
