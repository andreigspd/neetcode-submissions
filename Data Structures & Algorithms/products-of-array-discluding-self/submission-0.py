class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = [1] * n
        right_product = [1] * n
        left_product[0] = nums[0]
        right_product[n - 1] = nums[n - 1]
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i]
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i]

        ans = []
        for i in range(n):
            if i == 0:
                ans.append(right_product[i + 1])
            elif i == n - 1:
                ans.append(left_product[i - 1])
            else:
                ans.append(left_product[i - 1] * right_product[i + 1])
        return ans    