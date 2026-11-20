class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        target = {}
        for ch in t:
            target[ch] = target.get(ch, 0) + 1
        ans = ""
        left = 0
        have = 0
        freq_window = {}
        max_lg = float("inf")
        for right in range(len(s)):
            freq_window[s[right]] = freq_window.get(s[right], 0) + 1
            if s[right] in target.keys() and freq_window[s[right]] == target[s[right]]:
                have += 1
            while have == len(target):
                if (right - left + 1) < max_lg:
                    max_lg = (right - left + 1)
                    ans = s[left : right + 1]
                if s[left] in target.keys() and freq_window[s[left]] == target[s[left]]:
                    have -= 1
                freq_window[s[left]] -= 1
                left += 1
                
        return ans