class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = []
        count = Counter(s)
        for c, time in count.items():
            heapq.heappush(maxHeap, (-time, c))
        idle = None
        res = []
        while maxHeap:
            t, c = heapq.heappop(maxHeap)
            if idle: heapq.heappush(maxHeap, idle)
            res.append(c)
            if t + 1 < 0:
                idle = (t + 1, c)
            else:
                idle = None
        
        return "" if idle else "".join(res)