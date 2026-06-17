class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [(-cnt, c)for c, cnt in count.items()]
        heapq.heapify(maxHeap)
        preStatus = None # (-cnt, c)
        res = []
        while maxHeap:
            if maxHeap:
                cnt, c = heapq.heappop(maxHeap)
                res.append(c)
                if preStatus:
                    heapq.heappush(maxHeap, preStatus)
                    preStatus = None
                if cnt + 1 != 0:
                    preStatus = (cnt + 1, c)
        return "".join(res) if not preStatus else ""
                
