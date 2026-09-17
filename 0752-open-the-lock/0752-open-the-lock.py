class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        if "0000" in deadends: return -1
        if "0000" in target: return 0
        start = (0, 0, 0, 0)
        directions = [(1, 0, 0, 0), (-1, 0, 0, 0), (0, 1, 0, 0), (0, -1, 0, 0), (0, 0, 1, 0),  (0, 0, -1, 0),  (0, 0, 0, 1), (0, 0, 0, -1)]
        q = deque([start])
        visited = {"0000"}
        res = 0
        findTarget = False
        while q and not findTarget:
            for _ in range(len(q)):
                f, s, t, fo = q.popleft()
                for df, ds, dt, dfo in directions:
                    nf, ns, nt, nfo = self.transfer(f + df), self.transfer(s + ds), self.transfer(t + dt), self.transfer(fo + dfo)
                    cur = str(nf) + str(ns) + str(nt) + str(nfo)
                    if cur in visited: continue
                    if cur in deadends: continue
                    if cur == target: findTarget = True
                    visited.add(cur)
                    q.append((nf, ns, nt, nfo))
            res += 1
        return res if findTarget else -1
                
    def transfer(self, number):
        number = 0 if number == 10 else number
        number = 9 if number == -1 else number
        return number
