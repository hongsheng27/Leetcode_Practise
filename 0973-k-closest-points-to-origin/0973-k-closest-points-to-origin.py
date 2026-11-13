class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minHeap = [] # distance ** 2, x, y
        res = []
        for x, y in points:
            heapq.heappush(minHeap, (x ** 2 + y ** 2, x, y))
        for _ in range(k):
            dis, r, c = heapq.heappop(minHeap)
            res.append([r, c])
        return res
