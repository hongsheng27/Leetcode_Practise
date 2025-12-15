class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for [x, y] in points:
            heapq.heappush(distances, (x ** 2 + y ** 2, [x, y]))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(distances)[1])
        return res
        
