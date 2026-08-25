class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = y = d = best = 0
        directions = [
            (0, 1), # North
            (1, 0), # East
            (0, -1), # South
            (-1, 0) # West
        ]
        blocked = {(x, y) for x, y in obstacles}
        
        for command in commands:
            if command == -1: 
                d = (d + 1) % 4
            elif command == -2:
                d = (d - 1) % 4
            else:
                dx, dy = directions[d]
                for _ in range(command):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in blocked:
                        break
                    x, y = nx, ny
                best = max(best, x ** 2 + y ** 2)
        return best



            