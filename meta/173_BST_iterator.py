# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def left_traversal(self, node):
        self.stack.append(node)
        while node.left:
            self.stack.append(node.left)
            node = node.left

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.left_traversal(root)

    def next(self) -> int:
        top = self.stack.pop()

        if top.right:
            self.left_traversal(top.right)
        return top.val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Use a stack to store a subtree at all times to use only O(H) space.
# Append all the left nodes, and when we pop them, check if a right child exists, and append itself and its left subtree.