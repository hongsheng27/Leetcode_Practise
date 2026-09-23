class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        group = []
        for start, end in intervals:
            group.append((start, 1))
            group.append((end, -1))
        group.sort()
        room = maxRoom = 0
        for _, degree in group:
            room += degree
            maxRoom = max(room, maxRoom)
        return maxRoom

