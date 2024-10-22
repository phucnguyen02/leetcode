class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        cur = head
        next = cur.next
        res = None
        prev = None
        while cur and next:
            after_next = next.next
            next.next, cur.next = cur, after_next
            if prev: prev.next = next
            if not res: res = ListNode(0, next)

            prev = cur
            cur = cur.next
            if cur: next = cur.next
        
        return res.next
    
# If the list is less than 2 nodes long then return the head
# Keep 3 variables, the previous node, the current, and the next
# For each cur and next, cur.next = next.next, next.next = cur, and prev.next = next since next is now at the beginning of the pair
