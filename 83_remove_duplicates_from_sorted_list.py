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
    
    def remove_duplicates(self, head):
        if not head: return
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

if __name__ == "__main__":
    node_1 = ListNode(1)
    linked_list = LinkedList(node_1)
    linked_list.append_val(1)
    linked_list.append_val(1)
    linked_list.append_val(2)
    linked_list.append_val(2)
    linked_list.append_val(5)
    linked_list.append_val(6)
    linked_list.print_linked_list()
    linked_list.remove_duplicates(linked_list.head)
    linked_list.print_linked_list()


# Have 2 while loops, the outer one iterates each unique element of the linked list,
# the inner one keeps removing the next node which has the same value as the current one
# If list is empty, don't do anything

# cur = head
# while cur is not empty then
#   while cur.next is not empty and val of cur.next == val of cur then
#       remove cur.next
#       connect cur to the node after cur.next
#   cur = cur.next
# return cur