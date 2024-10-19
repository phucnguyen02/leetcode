class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        slow = head
        fast = head
        while n:
            n -= 1
            fast = fast.next
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        if prev:
            prev.next = slow.next
        else:
            return head.next
        
        return head
    
# Traverse to the end of the linked list, and go backwards
# Each time we go backwards, increment a counter. If the counter reaches n, remove that node
# We keep a reference of the previous node, and have the recursive function return the next node.
# If the previous node doesn't exist, then we are removing the head, so we return the next node.
# Otherwise, set the previous node's next pointer to be the next node, and return the current node.

# Iterative:
# Have fast and slow pointers that are n nodes apart, then iterate them both.
# Once fast has reached the end, we know slow is the node we have to remove.
# Keep track of the previous node from slow, and have its next pointer be slow's next.
# If prev is null then the node we are removing is the head node, so just return the node after head
# Otherwise, return the original head