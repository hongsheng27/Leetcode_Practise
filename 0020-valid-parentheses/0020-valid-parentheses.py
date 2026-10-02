class Solution:
    def isValid(self, s: str) -> bool:
        # () {} []
        # stack []
        # tc O(n) O(n)
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            elif stack and closeToOpen[c] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0




        