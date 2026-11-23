class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        n = len(nums)
        ans = []
        def bkt(start, curr):
            if len(curr) > n:
                return 
            ans.append(curr[:])
            for i in range(start, n):
                curr.append(nums[i])
                bkt(i + 1, curr)
                curr.pop()
        bkt(0, [])
        return ans
