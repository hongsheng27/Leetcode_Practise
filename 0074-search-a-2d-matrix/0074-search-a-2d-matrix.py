class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  
        top = 0
        bot = len(matrix) - 1
        row = -1
        while top <= bot:
            m = (top + bot) // 2
            if target < matrix[m][0]:
                bot = m - 1
            elif target > matrix[m][-1]:
                top = m + 1
            else:
                row = m
                break
        if row == -1: return False

        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
        return False
