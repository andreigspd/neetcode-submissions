class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "":
            return 0
        max_len = 0
        max_freq = 0
        max_freq_char = ""
        left = 0
        freq = {}
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            if freq[s[right]] > max_freq:
                max_freq = freq[s[right]]
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            max_len = right - left + 1
        return max_len
                
            
