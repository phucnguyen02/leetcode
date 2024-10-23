# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        cur_level = 0
        queue = [(root, 0)]
        res = []
        level_list = []
        while queue:
            node, level = queue.pop(0)
            if level != cur_level:
                res.append(level_list)
                level_list = []
                cur_level = level
            level_list.append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        res.append(level_list)

        for i in range(len(res)):
            if i % 2 != 0:
                res[i] = res[i][::-1]
        return res
    
# Traverse the binary tree by level
# For every odd level, reverse the list
