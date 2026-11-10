class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        # use maxHeap to pop highest cost action and give it to ladders
        # when bricks usage over bricks, start poping, laddders -= 1, once run out of bricks and ladders, stop
        maxHeap = []
        usage = r = 0
        while r < len(heights) - 1:
            diff = heights[r + 1] - heights[r] 
            if diff > 0:
                heapq.heappush(maxHeap, -diff)
                usage += diff
            if usage > bricks and ladders:
                replace = heapq.heappop(maxHeap)
                usage -= (-replace)
                ladders -= 1
            elif usage > bricks and not ladders:
                return r
            r += 1
        return r
            
            
            
        