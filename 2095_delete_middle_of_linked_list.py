class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, node):
        self.head = node
    
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
    
    def pop_node(self):
        if not self.head: return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None

    def delete_middle(self):
        if not self.head or not self.head.next: return None
        prev = None
        slow = fast = self.head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return self.head

if __name__ == "__main__":
    node_1 = ListNode(1)
    linked_list = LinkedList(node_1)
    linked_list.append_val(2)
    linked_list.append_val(4)
    linked_list.append_val(5)
    linked_list.delete_middle()
    linked_list.print_linked_list()
    linked_list.append_val(6)
    linked_list.append_val(7)
    linked_list.delete_middle()
    linked_list.print_linked_list()

# [1, 2, 4, 5]
# [1, 2, 4, 5, 6]

# Have 2 pointers, one that moves 1 step at a time and the other that moves 2 for traversal.
# Since the faster pointer moves twice as fast, when it reaches the end of the linked list or
# 1 step beyond, the slower pointer would be right in the middle of the list
# At the same time, we have a pointer right before the slower pointer so that when we have
# the middle of the list, we assign its next value to the node after the slower pointer

# If length of list is 0 or 1 then return an empty node

# slow = fast = head
# prev = null
# while fast and fast.next are not empty then
#   prev = slow
#   slow = slow.next
#   fast = fast.next.next
