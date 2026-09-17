class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        q = []
        ans = []
        left = 0
        for right in range(len(nums)):
            heapq.heappush_max(q, (nums[right], right))
            if right >= k - 1:
                top = heapq.heappop_max(q)
                while top[1] < left:
                    top = heapq.heappop_max(q)
                ans.append(top[0])
                heapq.heappush_max(q, top)
                left += 1
        return ans