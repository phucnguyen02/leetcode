class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root: return False
        return self.check_path(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def check_path(self, head, root):
        if not head: return True
        if not root: return False

        if head.val != root.val: return False
        return self.check_path(head.next, root.left) or self.check_path(head.next, root.right)
    
# Do DFS starting from every node as the potential start of the linked list. If node.val == head.val then we advance the linked list node. If the list node
# is null then we reached the end of the linked list, so we return true. If they're not equal then that is the end of this traversal.
# If we reach the end of the tree while the linked list is still going then return false
