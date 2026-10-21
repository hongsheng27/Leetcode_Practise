class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = defaultdict(list) # nth: (nth, t)
        for (u, v, w) in times:
            adj[u].append((v, w))
        minHeap = [(0, k)]
        visitNumber = 0
        visited = set()
        res = 0
        while minHeap:
            weight, nth = heapq.heappop(minHeap)
            
            if nth in visited: continue

            visited.add(nth)
            res = weight
            for nei, w in adj[nth]:
                heapq.heappush(minHeap, (weight + w, nei))
        return res if len(visited) == n else -1
        