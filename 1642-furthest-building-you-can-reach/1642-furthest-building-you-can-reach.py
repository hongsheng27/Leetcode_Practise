class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        minHeap = []
        for i in range(len(heights) - 1):
            gap = heights[i + 1] - heights[i]
            if gap > 0:
                heapq.heappush(minHeap, gap)
                if len(minHeap) > ladders:
                    bricks -= heapq.heappop(minHeap)
                    if bricks < 0:
                        return i
        return len(heights) - 1


                
        