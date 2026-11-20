class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def recursion(row, col):
            # base case
            if row == 1: return 0
            parent = recursion(row - 1, (col + 1) // 2)
            if col % 2 == 1:
                    return parent
            else:
                return 1 - parent
        return recursion(n, k)