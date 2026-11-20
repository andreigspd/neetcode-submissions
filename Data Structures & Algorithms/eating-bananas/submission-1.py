class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        left = 1
        right = max(piles)
        answer = -1
        while left <= right:
            rate = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += ceil(pile / rate)
            if hours <= h:
                answer = rate
                right = rate - 1
            else:
                left = rate + 1
        return answer
        
        