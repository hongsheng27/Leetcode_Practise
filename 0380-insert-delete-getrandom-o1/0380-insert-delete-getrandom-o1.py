class RandomizedSet:
    # use list to replace set
    # use hashmap to record index, so that remove can be O(1)
    def __init__(self):
        self.lst = []
        self.map = defaultdict(int) # val: index

    def insert(self, val: int) -> bool:
        if val in self.map: return False
        self.map[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map: return False
        index = self.map[val]
        n = len(self.lst)
        self.map[self.lst[n - 1]] = self.map[val]
        del self.map[val]
        self.lst[index], self.lst[n - 1] = self.lst[n - 1], self.lst[index]
        self.lst.pop()
        return True

    def getRandom(self) -> int:
        elem = random.choice(self.lst)
        return elem
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()