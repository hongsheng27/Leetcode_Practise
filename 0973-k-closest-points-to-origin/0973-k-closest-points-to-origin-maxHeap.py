class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for [x, y] in points:
            heapq.heappush(distances, (-((x ** 2) + (y ** 2)), [x, y]))
            if len(distances) > k:
                heapq.heappop(distances)
        
        return [d[1] for d in distances]
        
