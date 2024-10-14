"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        if not self.prev:
            self.head.right = root
        if self.prev:
            self.prev.right = root
        root.left = self.prev
        self.prev = root
        self.inorder(root.right)

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        self.head = ListNode(0)
        self.prev = None
        self.inorder(root)
        self.prev.right = self.head.right
        self.head.right.left = self.prev

        return self.head.right
    
# Because we want a sorted list from a BST, we have to do inorder traversal on the BST.
# We save a prev variable to store the node that we processed last so we may update its right pointer to the current node and our current node's left to be prev
# By default, prev is null, so if prev is null we connect the head node to the first node we process
# After the DFS, we reach the "tail" of the doubly linked list. We connect this tail to the head's right pointer, which is the first node of the list
# and we connect the node that the head points to's left pointer to be the tail so it creates the desired cycle.