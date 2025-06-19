class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = tokens.pop()
        if s not in "+-*/":
            return int(s)

        right = self.evalRPN(tokens)
        left = self.evalRPN(tokens)
        
        if s == "+":
            return left + right
        elif s == "-":
            return left - right
        elif s == "*":
            return left * right
        elif s == "/":
            return int(left / right)