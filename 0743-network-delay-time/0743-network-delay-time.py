class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        
        for src, dst, w in times:
            adj[src].append((dst, w))
        
        minHeap = [(0, k)] # (w, dst)
        shortest = {} # node: len
        while minHeap:
            w, dst = heapq.heappop(minHeap)
            if dst in shortest:
                continue
            shortest[dst] = w

            for node, cost in adj[dst]:
                heapq.heappush(minHeap, (w + cost, node))

        return max(shortest.values()) if len(shortest) == n else -1

        