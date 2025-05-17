class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                if i == "+":
                    stack.append(left + right)
                elif i == "-":
                    stack.append(left - right)
                elif i == "*":
                    stack.append(left * right)
                elif i == "/":
                    stack.append(int(left / right))
        return int(stack[0])