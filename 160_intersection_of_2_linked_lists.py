from collections import *

class Solution:
    # Brute force
    # def getIntersectionNode(self, headA, headB):
    #     a_nodes = defaultdict(int)
    #     cur_A = headA
    #     while cur_A:
    #         a_nodes[cur_A] = 1
    #         cur_A = cur_A.next
        
    #     cur_B = headB
    #     res = None
    #     while cur_B:
    #         if cur_B in a_nodes:
    #             res = cur_B
    #             break
    #         cur_B = cur_B.next
    #     return res      



    #O(1) space solution
    def get_length(self, head):
        if not head: return 0
        res = 0
        while head:
            res += 1
            head = head.next
        return res

    def getIntersectionNode(self, headA, headB):
        if not headB or not headA: return None
        len_A = self.get_length(headA)
        len_B = self.get_length(headB)
        diff = abs(len_A - len_B)

        if len_A > len_B:
            while diff:
                headA = headA.next
                diff -= 1
        else:
            while diff:
                headB = headB.next
                diff -= 1

        while headA and headB:
            if headA == headB: return headA
            headA = headA.next
            headB = headB.next
        return None

# Brute force: iterate 1 list, store each node in a dictionary,
# iterate through the other, find the first node that appears in the dictionary
# O(max(m, n)) time, O(min(m, n)) space

# O(1) space:
# Get length of both lists in O(max(m, n)) time
# Have 2 pointers for both lists, ptr1 and ptr2
# Suppose m > n, ptr1 corresponding to m, ptr2 corresponding to n
# Move the pointer of the longer list up so that n - index of ptr2 == m - index of ptr1
# Iterate ptr1 and ptr2 at the same time, stop when ptr1 == ptr2
# [1, 2, 3, 4, 5]
#    [6, 7, 4, 5]


# lenA = length of A, lenB = length of B
# diff = |lenA - lenB|
# if lenA > lenB then 
#   while diff then
#       headA = headA.next
#       diff -= 1
# else then
#   while diff then
#       headB = headB.next
#       diff -= 1
# while headA and headB then
#   if headA == headB then return either
#   headA = headA.next
#   headB = headB.next
# return null
