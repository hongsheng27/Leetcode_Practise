class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s) # (c, freq)
        maxHeap = [(-freq, c) for c, freq in count.items()]
        heapq.heapify(maxHeap)
        preStatus = None
        res = []
        while maxHeap or preStatus:
            if maxHeap:
                freq, c = heapq.heappop(maxHeap)
                res.append(c)
                if preStatus: 
                    heapq.heappush(maxHeap, preStatus)
                    preStatus = None
                if freq + 1 < 0: 
                    preStatus = (freq + 1, c)
            else:
                return ""
        return "".join(res)



