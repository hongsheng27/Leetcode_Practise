class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        start = (0, 0)
        direction = (0, 1)
        maxDistance = 0
        turnRight = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1)
        }
        turnLeft = {
            (0, 1): (-1, 0),
            (-1, 0): (0, -1),
            (0, -1): (1, 0),
            (1, 0): (0, 1)
        }
        obstacleSet = set()
        for x, y in obstacles:
            obstacleSet.add((x, y))

        def walk(x, y, direction, step):
            nx = x
            ny = y
            while step:
                x = x + direction[0]
                y = y + direction[1]
                if (x, y) in obstacleSet:
                    return (nx, ny)
                nx = x
                ny = y
                step -= 1
            return (nx, ny)
        
        for command in commands:
            if command == -1: 
                direction = turnRight[direction]
            elif command == -2:
                direction = turnLeft[direction]
            else:
                start = walk(start[0], start[1], direction, command)
                print(start)
                maxDistance = max(maxDistance, start[0]**2 + start[1]**2)
        return maxDistance



            