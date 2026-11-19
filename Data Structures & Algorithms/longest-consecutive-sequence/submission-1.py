class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        freq = {}
        longest_len = -1
        current_len = -1
        for x in nums:
            freq[x] = 1
        for x in nums:
            find = freq.get(x - 1, 0)
            if find == 0:
                current_len = 1
                x += 1
                while freq.get(x, 0) != 0:
                    current_len += 1
                    x += 1
                longest_len = max(longest_len, current_len)
        return longest_len

            