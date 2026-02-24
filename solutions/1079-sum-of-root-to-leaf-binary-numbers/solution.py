# 1. You must define the class
class Solution:
    # 2. The function must be inside the class and have 'self'
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, current_val):
            if not node:
                return 0
            
            # Binary logic: shift left and add current bit
            current_val = (current_val << 1) | node.val
            
            # If it's a leaf, return the calculated path value
            if not node.left and not node.right:
                return current_val
            
            # Recursive call for children
            return dfs(node.left, current_val) + dfs(node.right, current_val)
        
        return dfs(root, 0)

