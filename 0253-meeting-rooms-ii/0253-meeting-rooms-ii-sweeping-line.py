class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        time = []
        for start, end in intervals:
            time.append((start, 1))
            time.append((end, -1))

        time.sort()
        room = maxRoom = 0
        for t in time:
            room += t[1]
            maxRoom = max(maxRoom, room)
        return maxRoom