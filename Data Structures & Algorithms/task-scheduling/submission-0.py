class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import deque
        import heapq
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        max_heap = []
        q = deque()
        time = 0
        for task in freq.keys():
            heapq.heappush_max(max_heap, freq[task])
        while max_heap or q:
            time += 1
            if max_heap:
                freq = heapq.heappop_max(max_heap)
                freq -= 1
                if freq > 0:
                    q.append((freq, time + n))
            if q:
                freq, time_left = q.popleft()
                if time_left == time:
                    heapq.heappush_max(max_heap, freq)
                else:
                    q.appendleft((freq, time_left))
        return time