class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        def bkt(start, sum, path):
            if sum == target:
                ans.append(path[:])
                return
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                sum += nums[i]
                path.append(nums[i])
                if sum <= target:
                    bkt(i + 1, sum, path)
                sum -= nums[i]
                path.pop()
        bkt(0, 0, [])
        return ans