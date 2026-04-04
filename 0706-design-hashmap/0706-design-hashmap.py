class MyHashMap:
    def __init__(self):
        self.mapList = [-1 for _ in range(10**6)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.mapList)
        self.mapList[index] = value

    def get(self, key: int) -> int:
        index = key % len(self.mapList)
        return self.mapList[index]

    def remove(self, key: int) -> None:
        index = key % len(self.mapList)
        self.mapList[index] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)