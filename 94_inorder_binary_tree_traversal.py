class Solution:
    def __init__(self):
        self.res = []
    
    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)
        
        
    def inorderTraversal(self, root):
        self.dfs(root)
        return self.res

#In-order traversal = check left branch -> check current node val -> check right branch