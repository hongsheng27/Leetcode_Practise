class ListNode():
    def __init__(self, key= None, val= None):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.start, self.end = ListNode(), ListNode()
        self.start.next = self.end
        self.end.prev = self.start
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    def addToTail(self, node):
        tmp = self.end.prev
        self.end.prev.next = node
        node.next = self.end
        self.end.prev = node
        node.prev = tmp

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self.remove(node)
        self.addToTail(node)
        return node.val
       
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.addToTail(node)
            return
        node = ListNode(key, value)
        self.cache[key] = node
        self.addToTail(node)
        
        if len(self.cache) > self.capacity:
            lru = self.start.next
            self.remove(lru)
            del self.cache[lru.key]
        
        

        
        
       

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)