class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        n = len(nums)
        nums.sort()
        ans = []
        def bkt(start, curr):
            if len(curr) > n:
                return
            ans.append(curr[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                bkt(i + 1, curr)
                curr.pop()
        bkt(0, [])
        return ans
