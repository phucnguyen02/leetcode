# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def traverse(self, head, prev, n):
        if not head: return None
        
        next = self.traverse(head.next, head, n)
        self.count += 1
        if self.count == n:
            if not prev: return next
            prev.next = next
        return head
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.count = 0
        return self.traverse(head, None, n)
    
# Traverse to the end of the linked list, and go backwards
# Each time we go backwards, increment a counter. If the counter reaches n, remove that node
# We keep a reference of the previous node, and have the recursive function return the next node.
# If the previous node doesn't exist, then we are removing the head, so we return the next node.
# Otherwise, set the previous node's next pointer to be the next node, and return the current node.