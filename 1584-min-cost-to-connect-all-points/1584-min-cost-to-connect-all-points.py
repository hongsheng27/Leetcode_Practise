class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = { i : [] for i in range(len(points))}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append((distance, j))
                adj[j].append((distance, i))
        res = 0
        minHeap = [(0, 0)] # [(cost, point)]
        visit = set()
        while len(visit) < len(points):
            cost, dst = heapq.heappop(minHeap)
            if dst in visit: continue
            res += cost
            visit.add(dst)
            for n1, n2 in adj[dst]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (n1, n2))
        return res
            


        