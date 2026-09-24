class MedianFinder:
    import heapq
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
        elif num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush_max(self.max_heap, num)
        
        n = len(self.min_heap)
        m = len(self.max_heap)
        if n - m > 1:
            x = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, x)
        elif m - n > 1:
            x = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, x)

    def findMedian(self) -> float:
        n = len(self.min_heap)
        m = len(self.max_heap)
        if n == 0:
            return self.max_heap[0]
        elif m == 0:
            return self.min_heap[0]   
        if (n + m) % 2 == 1:
            if n > m:
                return self.min_heap[0]
            else:
                return self.max_heap[0]
        else:
            return (self.min_heap[0] + self.max_heap[0]) / 2
        