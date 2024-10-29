# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def set_parents(self, root):
        if not root:
            return

        if root.left:
            self.parent[root.left] = root
            self.set_parents(root.left)

        if root.right:
            self.parent[root.right] = root
            self.set_parents(root.right)


    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parent = {}

        self.set_parents(root)
        queue = [(target, 0)]
        res = []
        visited = set([target.val])
        while queue:
            node, dist = queue.pop(0)

            if dist == k:
                res.append(node.val)

            if node.left and node.left.val not in visited:
                queue.append((node.left, dist + 1))
                visited.add(node.left.val)

            if node.right and node.right.val not in visited:
                queue.append((node.right, dist + 1))
                visited.add(node.right.val)

            if node in self.parent and self.parent[node].val not in visited:
                queue.append((self.parent[node], dist + 1))
                visited.add(self.parent[node].val)

        return res
    
# Set up a hash table tracking the parent of every node, and then do BFS from the target