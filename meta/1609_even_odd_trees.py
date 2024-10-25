# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        level = 0
        while queue:
            prev = 1e9
            for i in range(len(queue)):
                node = queue.pop(0)

                if level % 2 == 0:
                    if node.val % 2 == 0: return False
                    if prev != 1e9 and node.val <= prev: return False
                else:
                    if node.val % 2 != 0: return False
                    if prev != 1e9 and node.val >= prev: return False

                prev = node.val
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            level += 1

        return True
    
# Do BFS to traverse every level. Store the previous node's value
# If the level is even, and the node's value isn't odd or its value is no more than the previous, return false
# If the level is odd, and the node's value isn't even or its value is no less than the previous, return false
# Only compare with the previous value if it's not the first node of the level