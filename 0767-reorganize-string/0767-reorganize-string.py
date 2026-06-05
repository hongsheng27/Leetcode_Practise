class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = [] # [-cnt, c]
        preStatus = [] # [-cnt, c]
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c, cnt in count.items():
            heapq.heappush(maxHeap, [-cnt, c])
        res = []
        while maxHeap:
            maxElem = heapq.heappop(maxHeap)
            maxElem[0] += 1

            if preStatus and preStatus[0] < 0:
                heapq.heappush(maxHeap, preStatus)

            preStatus = maxElem
            res.append(maxElem[1])

        return "".join(res) if len(res) == len(s) else ""
            
        