class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def recursion(row, col):
            # base case
            if row == 1: return 0
            child = recursion(row - 1, (col + 1) // 2)
            if child == 0:
                if col % 2 == 1:
                    return 0
                else:
                    return 1
            elif child == 1:
                if col % 2 == 1:
                    return 1
                else:
                    return 0

        return recursion(n, k)