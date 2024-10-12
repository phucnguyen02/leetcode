class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = [(root, 0)]
        cur_level = -1
        res = []
        prev = None
        while queue:
            node, level = queue.pop(0)
            if level != cur_level:
                if prev: res.append(prev.val)
                cur_level = level
            prev = node
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return res + [prev.val]
    
# Do BFS on the tree from left to right for each depth. 
# We store the last node we traversed to so that when we get to a new depth/level of the tree, we can add it to the result array since that's
# the rightmost node in that previous level