# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, cur = None, slow
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        first = head
        second = prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

# Do the tortoise and hare node trick
# The intuition is that the final list is the first half intertwined with the second half reversed
# So we go to the halfway point of the list, and reverse the second half.
# The tail of the first half is still connected to its next node, which is now the tail of the second half.
# Iterate through the lists to set the appropriate next pointer. We do not need to worry about the second half's tail since either
# the first half's tail or the second half's tail's before woul be connected to it still, depending on the length of the linked list.