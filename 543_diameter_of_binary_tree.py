class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def dfs(node):
            nonlocal diameter
            if not node: return 0

            left_path = dfs(node.left)
            right_path = dfs(node.right)

            diameter = max(diameter, left_path + right_path)
            return max(left_path, right_path) + 1
        dfs(root)
        return diameter
    
# The diameter is the longest left path + right path
# Use dfs to find the length of the paths of each subtree. The longest path for a node is 1 + max(left, right) to account for the edge leading into it