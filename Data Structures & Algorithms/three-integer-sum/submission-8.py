class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            mp = {}
            j = i + 1
            while j < n:
                target = - (nums[i] + nums[j])
                if target in mp:
                    ans.append([nums[i], target, nums[j]])
                    while j + 1 < n and nums[j] == nums[j + 1]:
                        j += 1
                mp[nums[j]] = j
                j += 1
        return ans
                    
                    