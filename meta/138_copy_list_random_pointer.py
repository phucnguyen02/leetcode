"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def clone(self, node):
        if node:
            if node not in self.visited:
                self.visited[node] = Node(node.val, None, None)
            return self.visited[node]
        return None
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        old = head
        new = Node(old.val, None, None)
        self.visited = {old: new}

        while old:
            new_next = self.clone(old.next)
            new_random = self.clone(old.random)

            new.next = new_next
            new.random = new_random

            new = new.next
            old = old.next
        return self.visited[head]
    
# For each node in the original list, we store the new node with the old as the key in a hash table
# Each time we clone the old node, we want to potentially create 2 new nodes corresponding to its next and random pointers.
# We store these nodes in the hash table as well, and have the next and random pointers of the new node point to them.
