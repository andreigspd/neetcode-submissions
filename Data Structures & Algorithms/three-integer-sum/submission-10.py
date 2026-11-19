class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        if max(nums) < 0:
            return []
        if min(nums) > 0:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            left = i + 1
            right = len(nums) - 1
            target = -nums[i]
            while left < right:
                current = nums[left] + nums[right]
                if current == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current < target:
                    left += 1
                else:
                    right -= 1
        return ans

                    