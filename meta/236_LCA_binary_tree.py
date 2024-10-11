class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = [root]
        ancestors = set()
        parents = {root: None}
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                parents[node.left] = node
            if node.right:
                queue.append(node.right)
                parents[node.right] = node
        while p:
            ancestors.add(p)
            p = parents[p]
        
        while q not in ancestors:
            q = parents[q]
        
        return q
    
# Use BFS to store the parent of every node in the tree
# Store all of the ancestors of p in a set
# Traverse upwards for q. The first ancestor of q that is also in p is the LCA