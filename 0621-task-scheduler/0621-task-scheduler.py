class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque() # time, cnt
        time = 0
        while maxHeap or q:
            time += 1
            while q and time == q[0][0]:
                _, c = q.popleft()
                heapq.heappush(maxHeap, c)
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                if freq + 1 < 0:
                    q.append((time + n + 1, freq + 1)) 
        return time