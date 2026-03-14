class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = [] # (pos, time)
        for i in range(len(position)):
            fleets.append((position[i], (target - position[i]) / speed[i] ))

        fleets.sort()
        stack = []
    
        for i in range(len(fleets) - 1, -1, -1):
            if stack and stack[-1] >= fleets[i][1]:
                continue
            stack.append(fleets[i][1])
        return len(stack)


