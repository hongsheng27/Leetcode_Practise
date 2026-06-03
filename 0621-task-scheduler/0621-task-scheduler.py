class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) - 1
        heap = list(count.values())
        heapq.heapify(heap)
        q = deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                freq = heapq.heappop(heap)
                if freq + 1 < 0:
                    q.append((freq + 1, time + n))
            while q and q[0][1] == time:
                cooldownElem = q.popleft()[0]
                heapq.heappush(heap, cooldownElem)
        return time

