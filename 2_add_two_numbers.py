# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def add(self, l1, l2, carry):
        if not l1 and not l2: 
            if carry: return ListNode(carry, None)
            return None
        l1_val = l2_val = 0
        l1_next = None
        l2_next = None
        if l1:
            l1_val = l1.val
            l1_next = l1.next
        
        if l2:
            l2_val = l2.val
            l2_next = l2.next

        sum = l1_val + l2_val + carry
        new_val = sum % 10
        new_carry = sum // 10
        return ListNode(new_val, self.add(l1_next, l2_next, new_carry))
    
    def addTwoNumbers(self, l1, l2):
        return self.add(l1, l2, 0)
        

# Iterate through each of the linked lists one by one. Add the values of the current nodes together while noting a carry for the next node.
# If a node is empty then treat its value as 0, and its next pointer is null.
# If both nodes are empty, we've reached the end of the linked lists. If the carry is 1 then add another node with the value 1, otherwise the node doesn't exist.