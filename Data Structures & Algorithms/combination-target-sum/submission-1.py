class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        def bkt(curr, sum):
            if sum == target:
                v = []
                for idx in curr[1:]:
                    v.append(nums[idx])
                ans.append(v)
                return
            for i in range(curr[-1], n):
                curr.append(i)
                sum += nums[i]
                if sum <= target:
                    bkt(curr, sum)
                sum -= nums[i]
                curr.pop()
        bkt([0], 0)
        return ans