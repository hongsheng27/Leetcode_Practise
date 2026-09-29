class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        minHeap = []
        c = 0
        trips.sort(key = lambda x: x[1])
        for passenger, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                e, p = heapq.heappop(minHeap)
                c -= p
            c += passenger
            heapq.heappush(minHeap, (end, passenger))
            if c > capacity:
                return False
        return True


        