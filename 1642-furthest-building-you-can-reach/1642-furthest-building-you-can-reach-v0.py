class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        # use maxHeap to pop highest cost action and give it to ladders
        # when bricks usage over bricks, start poping, laddders -= 1, once run out of bricks and ladders, stop
        # tc: O(N log N) sc: o(N)
        maxHeap = []
        usage = r = 0
        while r < len(heights) - 1:
            diff = heights[r + 1] - heights[r] 
            if diff > 0:
                heapq.heappush(maxHeap, -diff)
                usage += diff
            if usage > bricks:
                if not ladders:
                    return r
                replace = heapq.heappop(maxHeap)
                usage -= (-replace)
                ladders -= 1
            r += 1
        return r
            
            
            
        