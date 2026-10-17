from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        start = (0, 0, 0, 0)
        target = tuple(map(int, target))
        deadends = {tuple(map(int, d)) for d in deadends}

        if start in deadends:
            return -1

        q = deque([start])
        visited = {start}
        distance = 0

        while q:
            for _ in range(len(q)):
                cur = q.popleft()

                if cur == target:
                    return distance

                for i in range(4):
                    for step in (1, -1):
                        nextState = (
                            cur[:i]
                            + ((cur[i] + step) % 10,)
                            + cur[i + 1:]
                        )

                        if nextState in visited or nextState in deadends:
                            continue

                        visited.add(nextState)
                        q.append(nextState)

            distance += 1

        return -1