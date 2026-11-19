class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        if min(nums) > 0:
            return []
        if max(nums) < 0:
            return []
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            freq = {}
            j = i + 1
            while j < n:
                
                target = -nums[i] - nums[j]
                if target in freq:
                    ans.append([nums[i], target, nums[j]])
                    while j + 1 < n and nums[j] == nums[j + 1]:
                        j += 1
                freq[nums[j]] = j
                j += 1
        return ans


                    