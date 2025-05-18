class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(i, open_used = 0, close_used = 0):
            if len(i) == 2 * n:
                return res.append(i)
           
            if open_used < n:
                backtrack(i + '(',  open_used + 1, close_used)
            if close_used < open_used:
                backtrack(i + ')', open_used, close_used + 1)
            
        backtrack("")
        return res
