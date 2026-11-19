class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        if not nums:
            return []
        if k <= 0:
            return []
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        q = []
        for val, fr in freq.items():
            heapq.heappush(q, (fr, val))
            if len(q) > k:
                heapq.heappop(q)
        ans = []
        for fr, val in q:
            ans.append(val)
        return ans