# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return None
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left:
            left.right = root.right
            root.right = root.left
            root.left = None
        return right or left or root
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)

# After flattening the left subtree, we want to take its tail and connect it to the first node of the right subtree
# After connecting, return the flattened right subtree's tail so that it may be connected. If the right subtree doesn't exist
# then return the left subtree's tail. If neither exists then the root itself is the tail.
        