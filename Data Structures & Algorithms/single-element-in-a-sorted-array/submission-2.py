class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if ((mid - 1 < 0 or nums[mid - 1] != nums[mid]) and (mid + 1 == n or nums[mid] != nums[mid + 1])):
                return nums[mid]
            leftSize = mid - 1 if nums[mid - 1] == nums[mid] else mid
            if leftSize % 2:
                right = mid - 1
            else:
                left = mid + 1