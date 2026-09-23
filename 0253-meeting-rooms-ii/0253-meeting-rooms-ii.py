class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        events.sort()
        room = maxRoom = 0
        for _, change in events:
            room += change
            maxRoom = max(room, maxRoom)
        return maxRoom

