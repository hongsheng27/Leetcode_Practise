class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o == "+":
                stack.append(stack[-1] + stack[-2])
            elif o == "D":
                stack.append(stack[-1] * 2)
            elif o == "C":
                stack.pop()
            else:
                stack.append(int(o))
        total = 0
        for c in stack:
            total += int(c)
        return total
        