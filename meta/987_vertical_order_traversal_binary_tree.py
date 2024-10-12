# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, row, col):
        if not root: return
        self.min_col = min(self.min_col, col)
        self.max_col = max(self.max_col, col)
        self.cols[col].append((row, root.val))
        self.dfs(root.left, row + 1, col - 1)
        self.dfs(root.right, row + 1, col + 1)
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.min_col = 1e9
        self.max_col = -1e9
        self.cols = defaultdict(list)
        self.dfs(root, 0, 0)
        res = []
        for col in self.cols:
            self.cols[col].sort()
        for col in range(self.min_col, self.max_col + 1):
            cur = [val for (r, val) in self.cols[col]]
            res.append(cur)
        return res
        
# Do DFS and store the nodes in each column in a dict with a tuple (row, val)
# Sort each column at the end
# Each cell can have at most 1 collision so worst case scenario, just compare those 2 elements and figure out which one should go first

# Alternatively, do BFS. Use a dict with the column as they key and the value is a list of lists corresponding to each row
# We insert nodes into the list for a column based on its row. If a list has 2 elements (a collision), then compare which one is higher to put last

# Complexity should be O(N + W * H) with W and H being the width and height of the tree