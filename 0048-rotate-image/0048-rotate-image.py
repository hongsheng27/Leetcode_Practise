class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        TOP = LEFT = 0
        BOTTOM = RIGHT = len(matrix) - 1
        
        while LEFT < RIGHT and TOP < BOTTOM:
            for i in range(RIGHT - LEFT):
                tmp = matrix[TOP + i][LEFT]
                matrix[TOP + i][LEFT] = matrix[BOTTOM][LEFT + i]
                matrix[BOTTOM][LEFT + i] = matrix[BOTTOM - i][RIGHT]
                matrix[BOTTOM - i][RIGHT] = matrix[TOP][RIGHT - i]
                matrix[TOP][RIGHT - i] = tmp

            TOP += 1
            RIGHT -= 1
            LEFT += 1
            BOTTOM -= 1

        