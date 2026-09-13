class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            isCollide = False
            while stack and (stack[-1] > 0 and a < 0):
                if abs(stack[-1]) < abs(a):
                    stack.pop()
                    isCollide = False
                elif abs(stack[-1]) == abs(a):
                    isCollide = True
                    stack.pop()
                    break
                else:
                    isCollide = True
                    break
            if not isCollide: stack.append(a)
        return stack
                    
            
