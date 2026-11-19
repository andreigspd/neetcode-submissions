class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or len(numbers) == 1:
            return [-1, -1]
        left = 0
        right = len(numbers) - 1
        while True:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]
            elif current < target:
                left += 1
            else:
                right -= 1
            