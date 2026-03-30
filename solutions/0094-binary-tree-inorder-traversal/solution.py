class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)    # Traverse Left
            res.append(node.val)  # Visit Root
            dfs(node.right)   # Traverse Right
        
        dfs(root)
        return res

