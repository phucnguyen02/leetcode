# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        list_len = 0
        while cur:
            cur = cur.next
            list_len += 1
        res = []
        extra = list_len % k
        sublist_len = list_len // k if not extra else list_len // k + 1

        prev = None
        cur = head
        first = True
        count = 0
        while cur:
            if count == sublist_len:
                first = True
                extra -= 1
                count = 0
                prev.next = None
                if extra == 0:
                    sublist_len -= 1
                    
            if first:
                first = False
                res.append(cur)
            count += 1
            prev = cur
            cur = cur.next

        while len(res) < k:
            res.append(None)
        return res
    
# Length of each list is n // k, except the first n % k lists, which have an extra node
# Every time we have a counter reach n // k, set the previous node's pointer to be None (aka the tail of the first split linked list), and reset the counter