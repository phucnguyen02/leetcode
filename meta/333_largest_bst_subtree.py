# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root: return None
        root.is_bst = False
        root.size = 1
        root.min = root.val
        root.max = root.val

        left_max = -1e9
        right_min = 1e9
        left_BST = right_BST = True

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left:
            left_BST = left.is_bst
            root.size += left.size
            left_max = left.max
            root.min = min(root.val, left.min)

        if right:
            right_BST = right.is_bst
            root.size += right.size
            right_min = right.min
            root.max = max(root.val, right.max)

        
        if left_BST and right_BST and left_max < root.val < right_min:
            root.is_bst = True
            self.res = max(self.res, root.size)
        return root
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res
        

# Do DFS on every node
# At each node, initialize is_bst (whether the tree with the node as the root is a BST), min (the smallest value of the tree with the node as the root), size = 1 (size of tree), 
# and max (self-explanatory) properties for the node
# Also initialize variables left_max (largest value of left subtree), right_min (smallest value of right subtree), and booleans left_BST and right_BST indicating if the subtrees are BSTs

# Check the left subtree first
# Update the size of the tree, have left_max = left.max, and root.min = min(root.val, left.min) since the smallest value of the tree should be within the left subtree or the node itself.
# Do the same with the right subtree but with right_min = right.min and root.max = max(root.val, right.max) instead

# If both subtrees are BST and left_max < root.val < right_min then root is larger than every node in left and smaller than every node in right, so it's a BST.
# Set is_bst = true, and maximize the result
