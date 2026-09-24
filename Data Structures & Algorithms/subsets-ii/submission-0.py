class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        def bkt(start, path):
            ans.append(path[:])
            for i in range(start, n):
                if i > start and nums[i - 1] == nums[i]:
                    continue
                path.append(nums[i])
                bkt(i + 1, path)
                path.pop()
        bkt(0, [])
        return ans