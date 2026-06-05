class Solution:
    def reorganizeString(self, s: str) -> str:
        preStatus = [] # [-cnt, c]
        count = Counter(s)
        maxHeap = [[-cnt, c] for c, cnt in count.items()] # [-cnt, c]
        heapq.heapify(maxHeap)
        res = []
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            res.append(char)
            freq += 1

            if preStatus and preStatus[0] < 0:
                heapq.heappush(maxHeap, preStatus)

            preStatus = [freq, char]

        return "".join(res) if len(res) == len(s) else ""
            
        