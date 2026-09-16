class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {}
        mx = 0
        for x in nums:
            freq[x] = 1
        for x in nums:
            find = freq.get(x - 1, 0)
            if find == 0:
                count = 1
                x += 1
                while freq.get(x, 0) != 0:
                    count += 1
                    x += 1
                mx = max(mx, count)
        return mx
            
            