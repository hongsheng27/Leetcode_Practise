class ListNode:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def addToTail(self, node):
        prev = self.tail.prev
        node.prev = prev
        prev.next = node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache: 
            node = self.cache[key]
            self.remove(node)
            self.addToTail(node)
            return node.val
        else: return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) >= self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
            
        node = ListNode(key, value)
        self.cache[key] = node
        self.addToTail(node)
        

        
        
       

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)