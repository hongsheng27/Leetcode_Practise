class Node:
    def __init__(self, key=None, val: int = None):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.head = Node()
        self.tail = Node()
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
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._add_to_tail(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            if len(self.map) >= self.capacity:
                first = self.head.next
                self._remove(first)
                del self.map[first.key]

            new_node = Node(key, value)
            self.map[key] = new_node
            self._add_to_tail(new_node)
    




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)