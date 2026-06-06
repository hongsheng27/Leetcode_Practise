class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = [] # (position, passengerChange)
        for passengers, start, end in trips:
            events.append((start, passengers))
            events.append((end, -passengers))
        events.sort()
        cur = 0
        for e in events:
            cur += e[1]
            if cur > capacity: return False
        return True
