class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, node):
        self.head = node

    def get_length(self):
        if not self.head: return 0
        cur = self.head
        res = 0
        while cur:
            res += 1
            cur = cur.next
        return res
    
    def print_linked_list(self):
        arr = []
        cur = self.head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        print(arr)

    def append_val(self, val):
        if not self.head: 
            self.head = ListNode(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)
    
    def reverse_a_sublist(self, left, right):
        if left >= right: return self.head
        right = min(right, self.get_length() - 1)
        total = right - left + 1
        dummy = ListNode(-1, self.head)
        before_head = None
        rv_head = self.head
        while rv_head and left:
            left -= 1
            before_head = rv_head
            rv_head = rv_head.next

        rv_tail = self.head
        while rv_tail.next and right:
            right -= 1
            rv_tail = rv_tail.next
        after_tail = rv_tail.next        

        while total:
            prev_next = rv_head.next
            rv_head.next = after_tail
            after_tail = rv_head
            rv_head = prev_next
            total -= 1
        
        if not before_head: self.head = rv_tail
        else: before_head.next = rv_tail
        return dummy.next


if __name__ == "__main__":
    node_1 = ListNode(1)
    linked_list = LinkedList(node_1)
    linked_list.append_val(2)
    linked_list.append_val(4)
    linked_list.append_val(5)
    linked_list.append_val(9)
    linked_list.append_val(7)
    linked_list.print_linked_list()
    linked_list.reverse_a_sublist(2, 5)
    linked_list.print_linked_list()


#Have 4 variables, the one that stores the node before the head of the to-be-reversed sublist, the head of the sublist,
#the tail of the sublist, and the node after the tail.
#Iterate through each node of the sublist from left to right. The first node's next would be the node after the tail.
#The second node's next would be the first node, and so on and so forth.
#If left was originally 0, then the node before the sublist head would be empty, thus we update the head
#If right is larger than the length of the linked list, we have it be the last element of the sublist so as to have
#the right number of iterations.
#If left is larger than or equal to right then no reversal is necessary.



# if left >= right then return head
# right = min(right, length - 1)
# total = right - left + 1
# before_head = None
# rv_head = self.head
# while rv_head and left then
#     left -= 1
#     before_head = rv_head
#     rv_head = rv_head.next

# rv_tail = self.head
# while rv_tail.next and right then
#     right -= 1
#     rv_tail = rv_tail.next
# after_tail = rv_tail.next        

# while total:
#     prev_next = rv_head.next
#     rv_head.next = after_tail
#     after_tail = rv_head
#     rv_head = prev_next
#     total -= 1

# if before_head is empty then head = rv_tail
# else then before_head.next = rv_tail
# return head