class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        minHeap = []
        intervals.sort()
        for start, end in intervals:
            if minHeap and minHeap[0] <= start:
                heapq.heappop(minHeap)

            heapq.heappush(minHeap, end)
        return len(minHeap)
