# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        def bfs(root):
            q = deque()
            q.append(root)
            ans = []
            while q:
                n = len(q)
                curr = []
                for _ in range(n):
                    node = q.popleft()
                    curr.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                ans.append(curr[-1])
            return ans
        return bfs(root)