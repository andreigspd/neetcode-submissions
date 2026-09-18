class Node:
        def __init__(self, key=0, val=0):
            self.val = val
            self.key = key
            self.prev = None
            self.next = None
class LRUCache:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    def insert(self, node: Node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.cache) >= self.cap:
                lru = self.head.next
                self.remove(lru)
                del self.cache[lru.key]
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
        