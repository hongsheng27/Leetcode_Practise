class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif i == "-":
                right,left = int(stack.pop()), int(stack.pop())
                stack.append(left - right)
            elif i == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif i == "/":
                right,left = int(stack.pop()),int(stack.pop())
                stack.append(int(left / right))
            else:
                stack.append(i)
        return int(stack[0])