class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            isKeep = True
            while stack and (stack[-1] > 0 and a < 0) and isKeep:
                if abs(stack[-1]) < abs(a):
                    stack.pop()
                elif abs(stack[-1]) > abs(a):
                    isKeep = False
                else:
                    stack.pop()
                    isKeep = False
                
            if isKeep: stack.append(a)
        return stack
        