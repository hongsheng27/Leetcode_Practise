class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "]":
                string_q = deque()
                while stack and stack[-1] != "[":
                    string_q.appendleft(stack.pop())
                stack.pop()
                number_q = deque()
    
                while stack and self.isNumber(stack[-1]):
                    number_q.appendleft(stack.pop())
                stack = stack + list(int("".join(number_q)) * string_q)
                
            else:
                stack.append(c)
        return "".join(stack)
    def isNumber(self, c):
        return ord('0') <= ord(c) <= ord('9')
        