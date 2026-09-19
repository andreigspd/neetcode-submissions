# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.found = False
        def is_same_tree(p, q):
            if p is None and q is None:
                return True
            elif p is None:
                return False
            elif q is None:
                return False
            elif p.val != q.val:
                return False
            left = is_same_tree(p.left, q.left)
            right = is_same_tree(p.right, q.right)
            return left and right
        def dfs(root):
            if root:
                if is_same_tree(root, subRoot):
                    self.found = True
                    return
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.found