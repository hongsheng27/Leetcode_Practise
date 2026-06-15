class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque() # time, cnt
        time = 0
        while maxHeap or q:
            time += 1
            if q and time == q[0][0]:
                _, c = q.popleft()
                heapq.heappush(maxHeap, c)
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                if cnt + 1 != 0:
                    q.append((time + n + 1, cnt + 1)) 
        return time