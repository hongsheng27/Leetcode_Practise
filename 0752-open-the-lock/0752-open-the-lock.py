class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        # bfs to get shortest path
        # start from "0000", put every possible like "1000" to q
        # visited to prevent repeated
        # to list [0, 0, 0, 0], travese from 0 - 3, +- 1
        # need to hande 9 -> 0, 
        # if meet set(tuple(deadline)), continue, how doest that change compacity?
        # if meet tuple(target), return shortest distance
        # compancity => tc 10 * 10 / sc 10 * 10
        # 18:00
        q = deque([list("0000")])
        visited = set([tuple("0000")])
        deadends = {tuple(d) for d in deadends}
        target = tuple(target)
        if tuple("0000") in deadends: return -1
        distance = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if tuple(cur) == target: return distance
                
                for i in range(4):
                    for j in [1, -1]:
                        copy = cur.copy()
                        copy[i] = str((int(copy[i]) + j) % 10)
                        _copy = tuple(copy)
                        if _copy in visited or _copy in deadends: continue
                        visited.add(_copy)
                        q.append(copy)
            distance += 1
        return -1
        # 42:00 done, debug: 
        # 1. cur changed by every loop, need copy = cur.copy()
        # 2. type wrong, res = 0 if res == 10 else res
        # 3. "0000" in deadends
        # 58:40 ai-assist
        