class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import Counter
        freq = {}
        left = 0
        max_lg = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            while freq[s[right]] > 1 and left < right:
                freq[s[left]] -= 1
                left += 1
            max_lg = max(max_lg, right - left + 1)
        return max_lg