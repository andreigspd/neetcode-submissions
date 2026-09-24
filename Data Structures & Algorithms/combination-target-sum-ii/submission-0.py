class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        def bkt(curr, sum):
            if sum == target:
                v = []
                for idx in curr[1:]:
                    v.append(nums[idx])
                ans.append(v)
                return
            for i in range(curr[-1] + 1, n):
                if i > curr[-1] + 1 and nums[i] == nums[i - 1]:
                    continue
                curr.append(i)
                sum += nums[i]
                if sum <= target:
                    bkt(curr, sum)
                sum -= nums[i]
                curr.pop()
        bkt([-1], 0)
        return ans