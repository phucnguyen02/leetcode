class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root: return False
        return self.check_path(root, head)

    def check_path(self, node: Optional[TreeNode], head: Optional[ListNode]) -> bool:
        if not node: return False
        return self.dfs(node, head) or self.check_path(node.left, head) or self.check_path(node.right, head)

    def dfs(self, node: Optional[TreeNode], head: Optional[ListNode]) -> bool:
        if not head: return True 
        if not node: return False 
        if node.val != head.val:
            return False 
        return self.dfs(node.left, head.next) or self.dfs(node.right, head.next)
    
# Do DFS starting from every node as the potential start of the linked list. If node.val == head.val then we advance the linked list node. If the list node
# is null then we reached the end of the linked list, so we return true. If they're not equal then that is the end of this traversal.
# If we reach the end of the tree while the linked list is still going then return false
