class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtracking(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return 

            if openN < n:
                stack.append('(')
                backtracking(openN + 1, closedN)
                stack.pop()
            if openN > closedN:
                stack.append(')')
                backtracking(openN, closedN + 1)
                stack.pop()
        
        backtracking(0,0)
        return res