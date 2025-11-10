class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for c in s:
            if c not in close_to_open:
                stack.append(c)
            elif stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
