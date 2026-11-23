class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        if target < 0:
            return []
        candidates.sort()
        n = len(candidates)
        ans = []
        def bkt(start, sum, curr):
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                sum += candidates[i]
                curr.append(candidates[i])
                if sum <= target:
                    if sum == target:
                        ans.append(curr[:])
                    else:
                        bkt(i + 1, sum, curr)
                sum -= candidates[i]
                curr.pop()
        bkt(0, 0, [])
        return ans