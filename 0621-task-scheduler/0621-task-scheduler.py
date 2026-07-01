class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = deque() # (cnt, time)
        time = 0
        
        while maxHeap or q:
            time += 1
            while q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                if cnt + 1 < 0:
                    q.append((cnt + 1, time + n + 1))
        return time

        
