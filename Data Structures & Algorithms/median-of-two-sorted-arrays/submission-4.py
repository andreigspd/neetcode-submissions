class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n = len(nums1)
        m = len(nums2)
        left = 0
        right = n
        total = n + m
        half = total // 2
        while left <= right:
            mid = (left + right) // 2
            remaining = half - mid
            left1 = nums1[mid - 1] if mid > 0 else float("-inf")
            right1 = nums1[mid] if mid < n else float("inf")
            left2 = nums2[remaining - 1] if remaining > 0 else float("-inf")
            right2 = nums2[remaining] if remaining < m else float("inf")
            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    return float(min(right1, right2))
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = mid - 1
            elif left2 > right1:
                left = mid + 1
