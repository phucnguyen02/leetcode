# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, head, tail):
        if head == tail:
            return None
        self.reverse_list(head.next, tail)
        head.next.next = head
        head.next = None
        return head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        if k < 2: return head
        cur = head
        res = None
        k_cnt = k
        first = head
        prev_tail = None
        while cur:
            next_node = cur.next
            k_cnt -= 1
            if k_cnt == 0:
                k_cnt = k
                new_tail = self.reverse_list(first, cur)

                new_tail.next = next_node
                if prev_tail:
                    prev_tail.next = cur
                
                prev_tail = new_tail
                first = next_node
                if not res: res = cur

            cur = next_node
        return res

# If k < 2 then we don't do any reversing, just return the head
# Store a first pointer indicating the head of the list we're going to reverse, a prev_tail pointer indicating the tail of the last list we reversed
# cur is our current node pointer
# Everytime we iterate through k nodes, reset the counter. But when that happens, reverse the list from first to cur. The recursive function should return
# the new tail of the linked list, which was originally the first pointer. This new tail is now connected to cur's next pointer, with cur being the original tail
# of this list before we reversed it. The previous tail should now be connected to cur, cur being the new head of the reversed list.
# Update first to be the head node of the next list, and prev_tail to be our current tail
# If result is none then update res to be cur, which is the head of our new list