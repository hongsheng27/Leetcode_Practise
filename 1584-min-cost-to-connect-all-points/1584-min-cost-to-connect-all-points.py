class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = { i : [] for i in range(len(points))}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append((distance, j))
                adj[j].append((distance, i))
        cost = 0
        minHeap = [(0, 0)]
        visit = set()
        while minHeap:
            c, dst = heapq.heappop(minHeap)
            if dst in visit: continue
            cost += c
            visit.add(dst)
            for n1, n2 in adj[dst]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (n1, n2))
        return cost
            


        