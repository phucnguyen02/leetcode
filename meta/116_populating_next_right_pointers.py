"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        cur_level = 0
        prev = None
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)

            if level != cur_level:
                prev = None
                cur_level = level

            node.next = prev
            prev = node

            if node.right:
                queue.append((node.right, level + 1))
            
            if node.left:
                queue.append((node.left, level + 1))

        return root

# Do BFS traversal and store a previous node indicating the previous node we processed on the same level.
# Every time we traverse to a new level, have prev = None
# Have node.next = prev every time we process a new node, and traverse from right to left on each level so that the rightmost node points to None
