# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            if root is None:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        n = len(nodes)
        print(nodes)
        self.idx = 0
        def dfs():
            val = nodes[self.idx]
            self.idx += 1
            if val == "N":
                return None
            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
