class Allocator:
    def __init__(self, n: int):
        self.lst = [-1] * n 
        self.count = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        index = self.findConsecutiveFreeIndex(size)
        if index >= 0:
            for i in range(size):
                self.lst[index + i] = mID
                self.count[mID].append(index + i) 
        return index
        
    def freeMemory(self, mID: int) -> int:
        indices = self.count.get(mID, [])
        for i in indices:
            self.lst[i] = -1
        if mID in self.count:
            del self.count[mID]
        return len(indices)
    
    def findConsecutiveFreeIndex(self, size):
        r = 0
        while r < len(self.lst):
            total = 0
            start = r
            while r < len(self.lst) and self.lst[r] == -1:
                total += 1
                if total == size:
                    return start
                r += 1
            r += 1
        return -1


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)