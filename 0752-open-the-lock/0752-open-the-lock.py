class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        if "0000" in deadends: return -1
        if target == "0000": return 0
        directions = [(1, 0, 0, 0), (-1, 0, 0, 0), 
                      (0, 1, 0, 0), (0, -1, 0, 0),
                       (0, 0, 1, 0), (0, 0, -1, 0),
                       (0, 0, 0, 1), (0, 0, 0, -1)]
        deadends = set(deadends)
        q = deque([(0, 0, 0, 0)])
        visited = set()
        move = 0
        while q:
            for _ in range(len(q)):
                f, s, t, fo = q.popleft()
                for df, ds, dt, dfo in directions:
                    nf, ns, nt, nfo = self.transfer(f + df), self.transfer(s + ds), self.transfer(t + dt), self.transfer(fo + dfo)
                    cur = str(nf) + str(ns) + str(nt) + str(nfo)
                    if cur == target: return move + 1
                    if cur in deadends or cur in visited: continue
                    q.append((nf, ns, nt, nfo))
                    visited.add(cur)
            move += 1
        return -1
    def transfer(self, number):
        number = 0 if number == 10 else number
        number = 9 if number == -1 else number
        return number