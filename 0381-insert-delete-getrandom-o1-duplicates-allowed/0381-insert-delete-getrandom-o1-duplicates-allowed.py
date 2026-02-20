class RandomizedCollection:
    def __init__(self):
        self.arr = []
        self.count = {}

    def insert(self, val: int) -> bool:
        isExsit = True
        if val not in self.count:
            isExsit = False
            self.count[val] = set()
        self.arr.append(val)
        self.count[val].add(len(self.arr) - 1)
        return not isExsit

    def remove(self, val: int) -> bool:
        if val not in self.count:
            return False
        removeIndex = self.count[val].pop()
        lastNum = self.arr[len(self.arr) - 1]
        self.arr[removeIndex] = lastNum

        if removeIndex != len(self.arr) - 1:
            self.count[lastNum].remove(len(self.arr) - 1)
            self.count[lastNum].add(removeIndex)
        self.arr.pop()

        if not len(self.count[val]): del self.count[val]
        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()