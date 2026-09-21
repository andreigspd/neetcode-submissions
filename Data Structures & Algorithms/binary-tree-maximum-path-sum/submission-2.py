# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -1001
        def dfs(root):
            if root is None:
                return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            sum = root.val + left + right
            if sum > self.max_sum:
                self.max_sum = sum
            return root.val + max(left, right)
        dfs(root)
        return self.max_sum
