class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        n = len(nums)
        def bkt(start, curr):
            sol.append(curr[:])
            for i in range(start, n):
                curr.append(nums[i])
                bkt(i + 1, curr)
                curr.pop()
        bkt(0, [])
        return sol