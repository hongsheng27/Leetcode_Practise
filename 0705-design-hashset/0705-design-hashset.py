class MyHashSet:
    def __init__(self):
        self.setList = [[] for _ in range(1000)]
    def add(self, key: int) -> None:
        index = key % 1000
        for elem in self.setList[index]:
            if elem == key:
                return
        self.setList[index].append(key)
    def remove(self, key: int) -> None:
        index = key % 1000
        for i, elem in enumerate(self.setList[index]):
            if elem == key:
                self.setList[index].pop(i)
    def contains(self, key: int) -> bool:
        index = key % 1000
        for elem in self.setList[index]:
            if elem == key:
                return True
        return False

    

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)