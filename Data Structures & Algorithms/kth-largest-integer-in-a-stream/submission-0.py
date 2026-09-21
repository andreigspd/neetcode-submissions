class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        import heapq

        self.capacity = k
        self.q = []
        for x in nums:
            heapq.heappush(self.q, x)
        while len(self.q) > self.capacity:
            heapq.heappop(self.q)


    def add(self, val: int) -> int:
        import heapq
        heapq.heappush(self.q, val)
        if len(self.q) > self.capacity:
            heapq.heappop(self.q)
        return self.q[0]

