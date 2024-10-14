class Solution:
    def dfs(self, root, sum_path):
        if not root: return
        if not root.left and not root.right:
            self.sum += sum_path * 10 + root.val
            return
        
        sum_path = sum_path * 10 + root.val
        self.dfs(root.left, sum_path)
        self.dfs(root.right, sum_path)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.dfs(root, 0)
        return self.sum
    
# The sum path for each node would be the sum path of its parent * 10 + itself. If we reach a leaf node we update the global sum value