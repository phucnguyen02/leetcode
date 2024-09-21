# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        cur = ListNode()
        heap, res = [], cur
        for (i, head) in enumerate(lists):
            if head: heapq.heappush(heap, (head.val, i, head))

        while heap:
            val, i, head = heapq.heappop(heap)
            cur.next = head
            cur = cur.next
            if head.next:
                heapq.heappush(heap, (head.next.val, i, head.next))
        
        return res.next
    
# Use a priority queue. First add all of the heads into the queue. Each time we pop a node, it's going to be the next node in the final
# sorted list. We then add the next node for that head into the queue and we keep going.