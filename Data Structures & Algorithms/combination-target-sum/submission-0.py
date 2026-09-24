class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        x = []
        x.append(0)
        def bkt(level, sum):
            if sum == target:
                curr = []
                for i in range(1, level):
                    curr.append(nums[x[i]])
                ans.append(curr)
                return
            for i in range(x[level - 1], n):
                x.append(i)
                sum += nums[i]
                if sum <= target:
                    bkt(level + 1, sum)
                sum -= nums[i]
                x.pop()
        bkt(1, 0)
        return ans