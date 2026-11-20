class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        freq = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            if s[right] in freq:
                left = max(freq[s[right]] + 1, left)
            freq[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len