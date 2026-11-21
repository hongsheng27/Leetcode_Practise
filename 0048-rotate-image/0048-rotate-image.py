class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        TOP = LEFT = 0
        RIGHT = n - 1
        BOTTOM = n - 1

        while LEFT < RIGHT and TOP < BOTTOM:
            for i in range(RIGHT - LEFT):
                tmp = matrix[TOP][LEFT + i]
                matrix[TOP][LEFT + i] = matrix[BOTTOM - i][LEFT]
                matrix[BOTTOM - i][LEFT] = matrix[BOTTOM][RIGHT - i]
                matrix[BOTTOM][RIGHT - i] = matrix[TOP + i][RIGHT]
                matrix[TOP + i][RIGHT] = tmp
            TOP += 1
            RIGHT -= 1
            BOTTOM -= 1
            LEFT += 1


            
        
        
        