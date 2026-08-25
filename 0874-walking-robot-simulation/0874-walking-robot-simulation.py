class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        start = (0, 0)
        d = 0 # North
        maxDistance = 0
        directions = [
            (0, 1), # North
            (1, 0), # East
            (0, -1), # South
            (-1, 0) # West
        ]
     
        obstacleSet = set()
        for x, y in obstacles:
            obstacleSet.add((x, y))

        def walk(x, y, d, step):
            nx = x
            ny = y
            while step:
                x = x + directions[d][0]
                y = y + directions[d][1]
                if (x, y) in obstacleSet:
                    return (nx, ny)
                nx = x
                ny = y
                step -= 1
            return (nx, ny)
        
        for command in commands:
            if command == -1: 
                d = (d + 1) % 4
            elif command == -2:
                d = (d - 1) % 4
            else:
                start = walk(start[0], start[1], d, command)
                maxDistance = max(maxDistance, start[0]**2 + start[1]**2)
        return maxDistance



            