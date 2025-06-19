class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                right,left = stack.pop(), stack.pop()
                stack.append(left - right)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                right,left = stack.pop(), stack.pop()
                stack.append(int(left / right))
            else:
                stack.append(int(c))
        return stack[0]