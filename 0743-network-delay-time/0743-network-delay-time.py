class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        minHeap = [(0, k)]
        graph = defaultdict(list)
        for start, end, cost in times:
            graph[start].append((cost, end))
        visited = set()
        res = 0
        while minHeap:
            c, e = heapq.heappop(minHeap)

            if e in visited: continue

            visited.add(e)
            res = c
            
            for cost, end in graph[e]:
                heapq.heappush(minHeap, (c + cost, end))
       
        return res if len(visited) == n else -1
          
