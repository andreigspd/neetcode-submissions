class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i, x in enumerate(numbers):
            remaining = target - x
            left = i + 1
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == remaining:
                    return [i + 1, mid + 1]
                elif numbers[mid] < remaining:
                    left = mid + 1
                else:
                    right = mid - 1
        return []
