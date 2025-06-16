class Node:
    def __init__(self, key=None, val: int = None):
        self.val, self.key = val, key
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
    
    def _remove(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def _add_to_tail(self,node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_tail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            del self.cache[key]
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_tail(new_node)
        
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
    




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)