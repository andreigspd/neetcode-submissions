class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        freq_s1 = Counter(s1)
        n = len(s2)
        freq = {}
        left = 0
        for right in range(n):
            freq[s2[right]] = freq.get(s2[right], 0) + 1
            while left < right and (s2[left] not in freq_s1.keys() or freq[s2[left]] > freq_s1[s2[left]]):
                if freq[s2[left]] == 1:
                    del freq[s2[left]]
                else:
                    freq[s2[left]] -= 1
                left += 1
            if freq == freq_s1:
                return True
        return False

