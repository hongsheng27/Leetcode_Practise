class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(leftNum, rightNum, path):
            if leftNum == rightNum == n:
                res.append("".join(path))
                return
            if leftNum < n:
                path.append('(')
                backtrack(leftNum + 1, rightNum, path)
                path.pop()
            if leftNum > rightNum:
                path.append(')')
                backtrack(leftNum, rightNum + 1, path)
                path.pop()
        backtrack(0, 0, [])
        return res
        