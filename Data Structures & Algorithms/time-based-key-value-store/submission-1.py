class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.store[key]) - 1
        last_val = ""
        while left <= right:
            mid = (left + right) // 2
            if self.store[key][mid][1] <= timestamp:
                last_val = self.store[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return last_val