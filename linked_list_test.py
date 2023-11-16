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
    
    def insert(self, idx, val):
        if idx == 0:
            self.head = ListNode(val, self.head)
            return
        cur = self.head
        while cur.next and idx > 1:
            idx -= 1
            cur = cur.next
        next_node = cur.next
        cur.next = ListNode(val, next_node)

    def remove(self, idx):
        if not self.head: return
        if not idx:
            self.head = self.head.next
            return
        prev = None
        cur = self.head
        while cur.next and idx:
            idx -= 1
            prev = cur
            cur = cur.next
        prev.next = cur.next


if __name__ == "__main__":
    node_1 = ListNode(1)
    linked_list = LinkedList(node_1)
    linked_list.append_val(2)
    linked_list.append_val(4)
    linked_list.append_val(5)
    linked_list.print_linked_list()
    linked_list.pop_node()
    linked_list.print_linked_list()
    linked_list.insert(2, 6)
    linked_list.print_linked_list()
    linked_list.remove(1)
    linked_list.print_linked_list()
    
