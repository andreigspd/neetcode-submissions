class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        freq = 0
        ans = []
        def bkt(path):
            nonlocal freq
            if len(path) == n:
                ans.append(path[:])
                return
            for i in range(n):
                if not ((1 << i) & freq):
                    freq |= (1 << i)
                    path.append(nums[i])
                    bkt(path)
                    freq ^= (1 << i)
                    path.pop()
        bkt([])
        return ans