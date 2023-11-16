# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list2: return list1
        if not list1: return list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
# [1,2,4]
# [1,3,4]
# [1, 1, 2, 3, 4, 4]

# If the head of one list is less than the other's head, that smaller node's next node will be
# the result of the recursion call for mergeTwoLists containing the next of the smaller node on the original list and
# the other head.
# If one list is empty, the remaining values of the other would be the tail of the combined list.

# if list2 is empty then return list1
# if list1 is empty then return list2
# if head1 < head2 then head1.next = merge(head1.next, head2), return head1
# otherwise then head2.next = merge(head1, head2.next), return head2