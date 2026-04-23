class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            alive = True
            while stack and (stack[-1] > 0 and a < 0) and alive:
                if abs(stack[-1]) < abs(a):
                    stack.pop()
                elif abs(stack[-1]) > abs(a):
                    alive = False
                else:
                    stack.pop()
                    alive = False
                
            if alive: stack.append(a)
        return stack
        