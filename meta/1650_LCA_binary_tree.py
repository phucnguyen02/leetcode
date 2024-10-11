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
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_path = defaultdict(int)
        q_path = defaultdict(int)
        p_ptr, q_ptr = p, q
        while p_ptr:
            p_path[p_ptr.val] = p_ptr
            p_ptr = p_ptr.parent
        
        while q_ptr:
            q_path[q_ptr.val] = q_ptr
            q_ptr = q_ptr.parent

        for ptr in p_path:
            if ptr in q_path: return p_path[ptr]

# Trace the paths for each node going to the root. See which one is in common first.