# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        roots = set()
        delete = set(to_delete)

        def dfs(root):
            if not root: return None

            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if root.val in delete:
                if root.left:
                    roots.add(root.left)
                
                if root.right:
                    roots.add(root.right)

                return None

            return root

        dfs(root)
        if root.val not in delete: roots.add(root)
        return list(roots)
    
# Store final roots in a set. Do postorder traversal so we can get the left and right children before deleting a node.
# If the current node should be deleted, add the left and right children into the roots set if they're not null, then return null so the parent can have the accurate right/left pointers