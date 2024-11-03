# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def findIntersection(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        intersect = self.findIntersection(head)
        if not intersect: return None

        p1 = head
        p2 = intersect
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
    
# Use the tortoise and hare algorith mto see if there's a cycle, if yes then return the point in which they meet in the cycle
# Call this point x
# Say that before entering the cycle, the tortoise walks A steps, and walks another B before meeting the hare. In the cycle, the hare walks A + B + k*c steps, 
# with k being the number of times it goes through the cycle, and c being the cycle length
# Since the tortoise walked A + B steps, the hare walked 2(A + B) steps since it's twice as fast, and 2(A + B) = A + B + k * c  <-> A + B = k * c
# Currently the tortoise is B steps away from the cycle entrance, so it needs to walk A more steps to make it back to the cycle entrance because A + B = k * c
# Thus, we move the hare back to the beginning, and have it walk A steps as well to meet the tortoise again. The point they meet is the cycle entrance 