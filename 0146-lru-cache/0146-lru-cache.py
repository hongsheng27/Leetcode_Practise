class Node:
    def __init__(self, key = None, value = None):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    # structure
    # head = Node(key, value) = tail
    # map = {
    #     "key": Node
    # }
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def remove(self, node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

    def addToTail(self, node):
        before = self.tail.prev

        node.next = self.tail
        node.prev = before
        self.tail.prev = node
        before.next = node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.addToTail(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.remove(node)
            self.addToTail(node)
        else:
            newNode = Node(key, value)
            self.addToTail(newNode)
            self.map[key] = newNode
       
            # if over capacity, remove front
            if len(self.map) > self.capacity:
                lur = self.head.next
                self.remove(lur)
                del self.map[lur.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)