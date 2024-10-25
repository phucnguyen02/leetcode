# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self, root: TreeNode) -> int:
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root: TreeNode) -> int:
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None

        if key == root.val:
            if not root.left and not root.right: return None
            
            if root.right:
                root.val = self.successor(root.right)
                root.right = self.deleteNode(root.right, root.val)

            else:
                root.val = self.predecessor(root.left)
                root.left = self.deleteNode(root.left, root.val)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root


# When we remove a node from the BST, the one to take its place would be the first node smaller than it or the first node larger than it.
# In other words, it will be the rightmost child of its left child, or the leftmost child of its right child

# If the key is smaller than the root than traverse the left subtree, otherwise traverse the right subtree
# If key == root.val then find the predecessor (rightmost child of its left child) or the successor (leftmost child of its right child), whichever one's available.
# If neither is available then this is a leaf, so just return null
# Otherwise, replace the current node's val with the predecessor/successor's val, then remove that val by traversing the corresponding subtree it's in.