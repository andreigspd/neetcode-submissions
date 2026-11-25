class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start = 0
        max_len = 0

        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1

        for i in range(len(s)):
            start1, lg1 = helper(i, i)
            if lg1 > max_len:
                start = start1
                max_len = lg1
            start2, lg2 = helper(i, i + 1)
            if lg2 > max_len:
                start = start2
                max_len = lg2
            
        return s[start : start + max_len]