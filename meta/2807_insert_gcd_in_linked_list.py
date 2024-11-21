# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if not b: return a
            return gcd(b, a % b)
        if not head or not head.next: return head
        res = ListNode(0, head)
        cur_node = head
        next_node = head.next
        while next_node:
            gcd_node = ListNode(math.gcd(cur_node.val, next_node.val), next_node)
            cur_node.next = gcd_node
            cur_node = next_node
            next_node = next_node.next
        
        return res.next

# GCD function  
# def gcd(a, b):
#     if not b: return a
#     return gcd(b, a % b)