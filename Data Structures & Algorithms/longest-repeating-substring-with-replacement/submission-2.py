class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        freq = {}
        max_freq = 0
        max_len = 0
        for right in range(n):
            freq[s[right]] = freq.get(s[right], 0) + 1
            if freq[s[right]] > max_freq:
                max_freq = freq[s[right]]
            lg = right - left + 1
            
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
            
