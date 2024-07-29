from collections import defaultdict

class Solution:
    def verticalOrder(self, root):
        if not root: return []
        queue = []
        columns = defaultdict(list)
        queue.append((root, 0))
        min_level = 1e9
        max_level = -1e9
        while queue:
            node, level = queue.pop(0)
            if min_level > level: min_level = level
            if max_level < level: max_level = level

            columns[level].append(node.val)
            if node.left:
                queue.append((node.left, level - 1))
            
            if node.right:
                queue.append((node.right, level + 1))
        
        res = []
        for i in range(min_level, max_level + 1):
            res.append(columns[i])

        return res
    
# Do a BFS traversal. Store the node and its current level in a queue.
# The left child's level will be 1 less, and the right's will be 1 more.
# Store the nodes for each level in a hash table, while keeping track of the min and max levels for easier logging later