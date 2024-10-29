from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root: return []
        res = []
        queue = deque([root])
        while queue:
            queue_length = len(queue)
            for i in range(queue_length):
                node = queue.popleft()
                if i == queue_length - 1: res.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return res
    
# Do BFS on the tree from left to right for each depth. 
# We store the last node we traversed to so that when we get to a new depth/level of the tree, we can add it to the result array since that's
# the rightmost node in that previous level