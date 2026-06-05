class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = []
        q = deque()
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c, cnt in count.items():
            heapq.heappush(maxHeap, (-cnt, c))
        time = 0
        res = []
        while maxHeap:
            time += 1
            maxElem = heapq.heappop(maxHeap)
            newCnt = maxElem[0] + 1
            if newCnt < 0:
                q.append(((newCnt, maxElem[1]), time + 1))
            res.append(maxElem[1])
            while q and time == q[0][1]:
                (newCnt, val), t = q.popleft()
                heapq.heappush(maxHeap, (newCnt, val))
        if len(q): return ""
        return "".join(res)
            
        