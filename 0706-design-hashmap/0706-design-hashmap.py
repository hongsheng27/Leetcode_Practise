class MyHashMap:
    def __init__(self):
        self.mapList = [[] for _ in range(1009)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.mapList)
        for i, elem in enumerate(self.mapList[index]):
            k, v = elem
            if k == key:
                self.mapList[index].pop(i)       
        self.mapList[index].append((key, value))

    def get(self, key: int) -> int:
        index = key % len(self.mapList)
        for i, elem in enumerate(self.mapList[index]):
            k, v = elem
            print(k, v)
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = key % len(self.mapList)
        for i, elem in enumerate(self.mapList[index]):
            k, v = elem
            if k == key:
                self.mapList[index].pop(i)


        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)