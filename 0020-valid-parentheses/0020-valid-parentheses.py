class Solution(object):
    def isValid(self, s):
        if len(s) < 2: return False
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif not stack or stack[-1] != c:
                return False
            else:
                stack.pop()

        return len(stack) == 0

        