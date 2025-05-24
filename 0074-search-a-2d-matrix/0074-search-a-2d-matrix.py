class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = -1

        top, bot = 0, len(matrix) - 1
        while top <= bot:
            row = (bot + top) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False

        row = (bot + top) // 2
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            middle = (right + left) // 2
            if matrix[row][middle] < target:
                left = middle + 1
            elif matrix[row][middle] > target:
                right = middle - 1
            else:
                return True
        return False