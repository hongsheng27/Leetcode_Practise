class MyHashSet:
    def __init__(self):
        self.count = {}
    def add(self, key: int) -> None:
        self.count[key] = 1
    def remove(self, key: int) -> None:
        if key in self.count:
            del self.count[key]
    def contains(self, key: int) -> bool:
        return key in self.count


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)