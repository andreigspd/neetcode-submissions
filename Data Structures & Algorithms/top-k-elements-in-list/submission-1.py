class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        q = []
        for key, count in freq.items():
            heapq.heappush(q, (count, key))
            if len(q) > k:
                heapq.heappop(q)
        ans = []
        for _ in range(k):
            count, key = heapq.heappop(q)
            ans.append(key)
        return ans
