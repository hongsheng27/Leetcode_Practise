class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        group = []
        for passenger, start, end in trips:
            group.append((start, passenger))
            group.append((end, -passenger))
        group.sort()
        c = 0
        for g in group:
            c += g[1]
            if c > capacity: return False
        return True