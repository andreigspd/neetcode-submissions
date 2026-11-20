class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if s1 == "" and s2 != "":
            return False
        freq_s1 = {}
        for ch in s1:
            freq_s1[ch] = freq_s1.get(ch, 0) + 1
        
        freq_window = {}
        left = 0
        for right in range(len(s2)):
            freq_window[s2[right]] = freq_window.get(s2[right], 0) + 1
            if right < len(s1) - 1:
                continue
            if freq_s1 == freq_window:
                return True
            if freq_window[s2[left]] == 1:
                del freq_window[s2[left]]
            else:
                freq_window[s2[left]] -= 1
            left += 1
        return False    