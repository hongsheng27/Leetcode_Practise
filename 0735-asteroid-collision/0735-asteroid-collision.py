class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            alive = True
            while stack and (stack[-1] > 0 and a < 0) and alive:
                if stack[-1] < -a:
                    stack.pop()
                elif stack[-1] == -a:
                    alive = False
                    stack.pop()    
                else:
                    alive = False
                   
            if alive: stack.append(a)
        return stack
                    
            
