class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        q = []
        for key, count in freq.items():
            heapq.heappush_max(q, (count, key))
        ans = []
        for _ in range(k):
            count, key = heapq.heappop_max(q)
            ans.append(key)
        return ans
