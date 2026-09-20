class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [(-cnt, c)for c, cnt in count.items()]
        heapq.heapify(maxHeap)
        prev = None # (-cnt, c)
        res = []
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            res.append(char)
            freq += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if freq < 0:
                prev = (freq, char)
         
        return "".join(res) if not prev else ""
                
