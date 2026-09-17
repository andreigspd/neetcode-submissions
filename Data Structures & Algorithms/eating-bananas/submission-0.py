class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        left, right = 1, max(piles)
        ans = 0
        while left <= right:
            k = (left + right) // 2
            hours = 0
            for bananas in piles:
                hours += ceil(bananas / k)
            if hours > h:
                left = k + 1
            else:
                ans = k
                right = k - 1
        return ans
