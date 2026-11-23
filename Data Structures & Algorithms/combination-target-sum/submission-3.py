class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        if target < 0:
            return []
        n = len(nums)
        ans = []
        def bkt(start, sum, curr):
            for i in range(start, n):
                sum += nums[i]
                curr.append(nums[i])
                if sum <= target:
                    if sum == target:
                        ans.append(curr[:])
                    else:
                        bkt(i, sum, curr)
                curr.pop()
                sum -= nums[i]
        bkt(0, 0, [])
        return ans