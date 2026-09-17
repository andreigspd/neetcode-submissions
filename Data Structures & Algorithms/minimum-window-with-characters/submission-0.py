class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        freq_target = Counter(t)
        window = {}
        max_lg = float("inf")
        ans = [-1, -1]
        left = 0
        have = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in freq_target and freq_target[s[right]] == window[s[right]]:
                have += 1
            while have == len(freq_target):
                lg = right - left + 1
                if lg < max_lg:
                    max_lg = lg
                    ans = [left, right]

                window[s[left]] -= 1
                
                if s[left] in freq_target and window[s[left]] < freq_target[s[left]]:
                    have -= 1
                left += 1
        l, r = ans
        return s[l : r + 1] if ans != [-1, -1] else ""
            
