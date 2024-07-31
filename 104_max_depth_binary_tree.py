class Solution:
    def maxDepth(self, root) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
    
# If a node is empty then its depth is 0. Otherwise, the depth of a node is the max of the depths of its two children plus 1.