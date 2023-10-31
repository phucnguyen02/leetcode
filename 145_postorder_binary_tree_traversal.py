class Solution:
    def __init__(self):
        self.res = []
    
    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        self.dfs(root.right)
        self.res.append(root.val)
           
    def preorderTraversal(self, root):
        self.dfs(root)
        return self.res

#Preorder traversal = check left branch -> check right branch -> check current node val