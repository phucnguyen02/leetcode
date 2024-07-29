from collections import defaultdict

class DoublyLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DoublyLinkedList(0, 0)
        self.tail = DoublyLinkedList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = defaultdict(int)
    
    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)


    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node: return -1
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)

        if not node:
            new_node = DoublyLinkedList(key, value)
            self.cache[key] = new_node
            self.add_node(new_node)
            self.capacity -= 1
            if self.capacity < 0:
                last = self.tail.prev
                self.remove_node(last)
                self.cache.pop(last.key)
                self.capacity += 1
        else:
            node.val = value
            self.move_to_head(node)
        
# Use a doubly linked list to store the usage of the keys. Head means most recently used, tail means least recently used.
# Use a hash table to store the nodes for retrieval in O(1).

# Each time a node is interacted with, it gets moved to the front of the linked list
# For the get function, we check if the node exists first. If so, move it to the head, otherwise return -1
# For the put function, we check if the node exists first. If so, update its value and move it to the head.
# Otherwise, create a new node, store it in the hash map. If adding the node exceeds the capacity, pop the tail node.
