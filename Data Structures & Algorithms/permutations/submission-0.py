class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        freq = [0] * n
        ans = []
        def bkt(path):
            if len(path) == n:
                ans.append(path[:])
                return
            for i in range(n):
                if freq[i] == 0:
                    freq[i] = 1
                    path.append(nums[i])
                    bkt(path)
                    freq[i] = 0
                    path.pop()
        bkt([])
        return ans