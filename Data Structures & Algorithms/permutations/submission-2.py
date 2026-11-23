class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        n = len(nums)
        ans = []
        used = set()
        def bkt(level, curr):
            if level == n:
                ans.append(curr[:])
                return
            for i in range(n):
                if i not in used:
                    curr.append(nums[i])
                    used.add(i)
                    bkt(level + 1, curr)
                    used.remove(i)
                    curr.pop()
        bkt(0, [])
        return ans