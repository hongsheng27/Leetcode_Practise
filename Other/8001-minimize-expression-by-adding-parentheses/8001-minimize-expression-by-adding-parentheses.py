class Solution:
    def minimizeExpression(self, expression: str) -> int:
        res = float('inf')
        plusIndex = expression.index('+')
        for x in range(plusIndex):
          for y in range(len(expression) - 1,plusIndex ,-1):
            left = expression[:x]
            right = expression[y + 1:]
            start = int(left) if left else 1
            end = int(right) if right else 1
            middle = int(expression[x: plusIndex]) + int(expression[plusIndex + 1:y + 1])
            res = min(res, start * middle * end)
        return res
