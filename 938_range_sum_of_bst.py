class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def dfs(node, low, high):
            nonlocal res
            if not node: return
            if node.val < low:
                dfs(node.right, low, high)
            elif node.val > high:
                dfs(node.left, low, high)
            else:
                res += node.val
                dfs(node.left, low, high)
                dfs(node.right, low, high)
        dfs(root, low, high)
        return res
    
# Could just traverse through the entire BST to find nodes that are between low and high
# Save time by discarding subtrees that are outside of the range
# If node.val < low then the entire left subtree is smaller than low, ignore it
# If node.right > high then the entire right subtree is higher than high, ignore it