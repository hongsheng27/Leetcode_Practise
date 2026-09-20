class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            alive = True
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if stack[-1] == -(asteroids[i]):
                    stack.pop()
                    alive = False
                    break
                elif stack[-1] > -(asteroids[i]):
                    alive = False
                    break
                else:
                    stack.pop()
            if alive: stack.append(asteroids[i])
        return stack