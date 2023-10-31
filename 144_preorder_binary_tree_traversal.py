class Solution:
    def __init__(self):
        self.res = []
    
    def dfs(self, root):
        if not root: return
        self.res.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)
           
    def preorderTraversal(self, root):
        self.dfs(root)
        return self.res

#Preorder traversal = check current node val -> check left branch -> check right branch