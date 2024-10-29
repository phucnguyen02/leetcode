class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.next = None
        self.prev = None

class AllOne:

    def __init__(self):
        self.head = Node(-1e9)
        self.tail = Node(1e9)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.map = {}

    def inc(self, key: str) -> None:
        if key in self.map:
            cur = self.map[key]
            freq = cur.freq
            cur.keys.remove(key)

            if cur.next.freq != freq + 1:
                new = Node(freq + 1)
                new.next = cur.next
                new.prev = cur

                cur.next.prev = new
                cur.next = new
                new.keys.add(key)
                self.map[key] = new

            else:
                cur.next.keys.add(key)
                self.map[key] = cur.next

            if not cur.keys:
                self.remove(cur)
        else:
            if self.head.next.freq > 1:
                new = Node(1)
                new.next = self.head.next
                self.head.next.prev = new

                new.prev = self.head
                self.head.next = new

                new.keys.add(key)
                self.map[key] = new
            else:
                self.head.next.keys.add(key)
                self.map[key] = self.head.next

        
    def dec(self, key: str) -> None:
        if key not in self.map:
            return  # Key does not exist

        node = self.map[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:
            # Remove the key from the map if freq is 1
            del self.map[key]
        else:
            prevNode = node.prev
            if prevNode.freq != freq - 1:
                # Create a new node if the previous node does not exist or freq is not freq - 1
                newNode = Node(freq - 1)
                newNode.keys.add(key)
                newNode.prev = prevNode
                newNode.next = node
                prevNode.next = newNode
                node.prev = newNode
                self.map[key] = newNode
            else:
                # Decrement the existing previous node
                prevNode.keys.add(key)
                self.map[key] = prevNode

        # Remove the node if it has no keys left
        if not node.keys:
            self.remove(node)
        
    
    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev        

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head: return ""
        return list(self.tail.prev.keys)[0]
        

    def getMinKey(self) -> str:
        if self.head.next == self.tail: return ""
        return list(self.head.next.keys)[0]
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# Use a doubly linked list where the head has the min key and the tail has the max key
# Whenever we increment, if the key doesn't exist then it is either the new head with freq 1 or add the key to the node with freq 1
# If it does exist then find its node and create a node with freq + 1 if it doesn't exist or add it to the node with freq 1
# Do the same with decrement, except when freq = 0 we remove the node from the hash table storing the node's key

# If at any point a node doesn't have any keys, remove it from the linked list
