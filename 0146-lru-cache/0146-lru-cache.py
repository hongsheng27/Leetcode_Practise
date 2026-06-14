class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = {}
        self.start = Node()
        self.end = Node()
        self.start.next = self.end
        self.end.prev = self.start
    def delete(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def moveToTail(self, node):
        prev = self.end.prev
        node.next = self.end
        self.end.prev = node 
        prev.next = node
        node.prev = prev

    def get(self, key: int) -> int:
        if key not in self.count: return -1
        node = self.count[key]
        self.delete(node)
        self.moveToTail(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)
        if key in self.count:
            self.delete(self.count[key])
            self.moveToTail(newNode)
            self.count[key] = newNode
        else:
            self.count[key] = newNode
            self.moveToTail(newNode)
            if len(self.count) > self.capacity:
                oldNode = self.start.next
                del self.count[oldNode.key]
                self.delete(oldNode)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)