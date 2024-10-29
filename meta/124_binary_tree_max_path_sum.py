# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            nonlocal res

            if not root: return 0
            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)

            res = max(res, root.val + left_max + right_max)

            return root.val + max(left_max, right_max)

        dfs(root)
        return res
    
# At each node, calculate the max path sum of the left and right subtrees.
# We also update the result by maximizing it vs. the sum from combining both paths + the root. However, we discard negative paths
# We return the sum of the root + the max path because when we go to the parent, we cannot account for going through both paths, only 1.