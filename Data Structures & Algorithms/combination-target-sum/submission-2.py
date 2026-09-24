class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        def bkt(start, sum, path):
            if sum == target:
                ans.append(path[:])
                return
            for i in range(start, n):
                path.append(nums[i])
                sum += nums[i]
                if sum <= target:
                    bkt(i, sum, path)
                sum -= nums[i]
                path.pop()
        bkt(0, 0, [])
        return ans