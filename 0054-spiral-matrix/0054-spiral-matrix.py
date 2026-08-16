class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        lst = []
        while left <= right and top <= bottom:
            for col in range(left, right + 1): 
                lst.append(matrix[top][col])
            top += 1
            if top > bottom: break
            for row in range(top, bottom + 1):
                lst.append(matrix[row][right])
            right -= 1
            if left > right: break
            for col in range(right, left - 1, -1):
                lst.append(matrix[bottom][col])
            bottom -= 1
            for row in range(bottom, top - 1, -1):
                lst.append(matrix[row][left])
            left += 1
        return lst

