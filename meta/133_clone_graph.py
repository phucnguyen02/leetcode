"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def dfs(self, node, visited):
        visited.add(node)
        for neighbor in node.neighbors:
            self.neighbors[node.val].append(neighbor.val)
            if neighbor not in visited:
                self.dfs(neighbor, visited)
            

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        if not node.neighbors: return Node(node.val)
        self.neighbors = defaultdict(list)
        self.dfs(node, set())
        nodes = {key: Node(key) for key in self.neighbors}
        for cur in nodes:
            cur_node = nodes[cur]
            for neighbor in self.neighbors[cur]:
                cur_node.neighbors.append(nodes[neighbor])
        return nodes[node.val]
    
# First we use dfs to store all of the nodes and their neighbors in an easily accessible hash table
# Next, we create new nodes for each key in the hash table
# After that, iterate through each one of those nodes, get its value, and add all of its neighbors to it based on the neighbors hash table