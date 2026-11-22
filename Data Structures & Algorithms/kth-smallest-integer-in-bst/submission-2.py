# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        self.ans, self.cnt = 0, k

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.cnt == 0:
                return
            self.cnt -= 1
            if self.cnt == 0:
                self.ans = root.val
                return
            dfs(root.right)
        dfs(root)
        return self.ans
            