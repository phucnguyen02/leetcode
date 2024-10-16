# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, sum, path):
        if not root: return
        
        sum -= root.val
        path.append(root.val)
        if not sum and not root.left and not root.right:
            self.res.append(list(path))
     
        self.dfs(root.left, sum, path)
        self.dfs(root.right, sum, path)
        
        path.pop()
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        self.res = []
        self.dfs(root, targetSum, [])
        return self.res