class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = top = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        while left <= right and top <= bottom:
            if matrix[top][right] == target: return True
            if target < matrix[top][right]:
                right -= 1
            elif target > matrix[top][right]:
                top += 1
        return False
            