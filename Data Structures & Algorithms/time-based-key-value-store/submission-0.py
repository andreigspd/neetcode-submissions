class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.mp[key]) - 1
        last_val = ""
        while left <= right:
            mid = (left + right) // 2
            if self.mp[key][mid][1] <= timestamp:
                last_val = self.mp[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return last_val