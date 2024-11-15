"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        while node.parent and node.parent.right == node:
            node = node.parent
        return node.parent
    
# If the node has a right subtree, the successor is the leftmost node of the right subtree
# If it doesn't, it's somewhere in the parent. Keep climbing the tree until the current node is in the left subtree, then the parent is the successor