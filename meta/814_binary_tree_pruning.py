class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if not root.left and not root.right and not root.val:
            return None
        
        return root
    
# If both subtrees are empty and the root itself isn't 0 then prune it by returning null, otherwise return the root