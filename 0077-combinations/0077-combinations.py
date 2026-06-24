class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(num, path):
            # base case
            if len(path) == k:
                res.append(path.copy())
                return
            if num > n: return 
            # recursion case
            path.append(num)
            backtrack(num + 1, path)
            path.pop()

            backtrack(num + 1, path)
        backtrack(1, [])
        return res