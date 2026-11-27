class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key = lambda x : x[0])
        i = 1
        current = intervals[0]
        ans = []
        while i < n:
            if intervals[i][0] <= current[1]:
                current[1] = max(current[1], intervals[i][1])
            else:
                ans.append(current)
                current = intervals[i]
            i += 1
        ans.append(current)
        return ans