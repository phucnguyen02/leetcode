class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        if head.next == head:
            node = Node(insertVal, head)
            head.next = node
            return head

        prev = head
        cur = head.next
        insert = False
        while True:
            if prev.val <= insertVal <= cur.val: insert = True
            elif prev.val > cur.val:
                if insertVal >= prev.val or insertVal <= cur.val:
                    insert = True
            
            if insert:
                prev.next = Node(insertVal, cur)
                return head
            prev = cur
            cur = cur.next
            if prev == head: break
        prev.next = Node(insertVal, cur)
        return head
    
# Edge cases:
# Empty list -> return a new node that points to itself
# List with 1 node -> return the head that points to the new node and the new node points to the head
# Otherwise:
# Use 2 pointers for the previous node and current node.
# If prev.val <= insert <= cur.val then we can insert the node here to maintain order
# If prev.val > cur.val then we're at the end of the sorted list and looping back to the beginning. Here we can insert either the new largest node or the new smallest node.
# If neither of this happens then the max would be the same as the min of the list, so the list only has 1 value. Then we can insert the node anywhere in the list.