class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        from collections import Counter
        freq1 = Counter(s1)
        freq2 = Counter()
        for right in range(m):
            freq2[s2[right]] += 1
            if right >= n:
                left = s2[right - n]
                if freq2[left] == 1:
                    del freq2[left]
                else:
                    freq2[left] -= 1
            if freq1 == freq2:
                return True
        return False

