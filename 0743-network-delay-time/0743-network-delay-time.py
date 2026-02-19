class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for src, dst, w in times:
            adj[src].append((w, dst)) # [(distance, dst)]

        minHeap = [(0, k)] # [(distance, dst)]
        shortest = {}

        while minHeap:
            w, dst = heapq.heappop(minHeap)
            if dst in shortest: continue
            shortest[dst] = w
            
            for cost, node in adj[dst]:
                heapq.heappush(minHeap, (w + cost, node))

        return max(shortest.values()) if len(shortest) == n else -1

