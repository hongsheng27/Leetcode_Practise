class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = defaultdict(list) # nth: (nth, t)
        for (u, v, w) in times:
            adj[u].append((v, w))
        minHeap = [(0, k)]
        visitNumber = 0
        visited = set()
        while minHeap:
            weight, nth = heapq.heappop(minHeap)
            
            if nth in visited: continue

            visited.add(nth)
            visitNumber += 1
            if visitNumber == n: return weight
            for nei, w in adj[nth]:
                heapq.heappush(minHeap, (weight + w, nei))
        return -1
        