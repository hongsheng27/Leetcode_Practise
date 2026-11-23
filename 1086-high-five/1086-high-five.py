class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        scoreMap = {}  # {id: minHeap}
        for _id, score in items:
            if _id not in scoreMap:
                scoreMap[_id] = []
            
            heapq.heappush(scoreMap[_id], score)
            
            if len(scoreMap[_id]) > 5:
                heapq.heappop(scoreMap[_id])

        res = []
        for _id, scores in scoreMap.items():
            res.append([_id, sum(scores) // len(scores)])
        return sorted(res)
            
           