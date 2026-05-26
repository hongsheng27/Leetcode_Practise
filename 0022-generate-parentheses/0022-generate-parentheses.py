class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def backtrack(left, right, stack):
            if left == right == n:
                self.res.append("".join(stack))
                return
            if left < n:
                stack.append('(')
                backtrack(left + 1, right, stack)
                stack.pop()
            if right < n and left > right:
                stack.append(')')
                backtrack(left, right + 1, stack)
                stack.pop()
        backtrack(0, 0, [])
        return self.res
        