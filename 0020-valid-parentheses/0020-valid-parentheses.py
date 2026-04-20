class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        for b in s:
            if stack and b in closeToOpen and stack[-1] == closeToOpen[b]:
                stack.pop()
            else:
                stack.append(b)
        return True if not stack else False
        