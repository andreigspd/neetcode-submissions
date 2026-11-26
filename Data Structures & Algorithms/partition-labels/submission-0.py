class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first = {}
        last = {}
        for idx, char in enumerate(s):
            if char not in first:
                first[char] = idx
            last[char] = idx
        res = []
        curr_end = last[s[0]]
        lg = 0
        for i in range(len(s)):
            lg += 1
            if last[s[i]] > curr_end:
                curr_end = last[s[i]]
            if i == curr_end:
                res.append(lg)
                lg = 0
                curr_end = -1
        return res
