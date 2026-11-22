class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.capacity = k
        self.q = []
        for x in nums:
            heapq.heappush(self.q, x)
        while (len(self.q) > k):
            heapq.heappop(self.q)
    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        if len(self.q) > self.capacity:
            heapq.heappop(self.q)
        return self.q[0]
