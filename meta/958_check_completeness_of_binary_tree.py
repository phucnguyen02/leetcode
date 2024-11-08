# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        levels = defaultdict(list)

        queue = [(root, 0)]
        level = 0
        while queue:
            for i in range(len(queue)):
                node, idx = queue.pop(0)
                levels[level].append(idx)
                if node.left:
                    queue.append((node.left, idx * 2))
                if node.right:
                    queue.append((node.right, idx * 2 + 1))
            
            if queue and len(levels[level]) != 2 ** level: return False
            if levels[level][0] != 0: return False
            for i in range(len(levels[level]) - 1):
                if levels[level][i] != levels[level][i + 1] - 1:
                    return False
            level += 1
        
        return True
    
# Store each level in hash table
# If the level isn't the last and its length is different from 2^level, return false
# If the first node in a level is not index 0 then return False
# Check every node in the level to see if it's 1 more than the previous.