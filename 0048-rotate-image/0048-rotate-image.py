class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        TOP = LEFT = 0
        BOTTOM = RIGHT = len(matrix) - 1
   
        while LEFT < RIGHT and TOP < BOTTOM:
            q = deque()
            for c in range(LEFT, RIGHT + 1):
                q.append(matrix[TOP][c])
        
            for r in range(TOP + 1, BOTTOM + 1):
                q.append(matrix[r][RIGHT])
    
            for c in range(RIGHT - 1, LEFT - 1, -1):
                q.append(matrix[BOTTOM][c])

            for r in range(BOTTOM - 1, TOP, -1):
                q.append(matrix[r][LEFT])
            
            for _ in range(RIGHT - LEFT):
                q.appendleft(q.pop())
            
            i = 0
            for c in range(LEFT, RIGHT + 1):
                matrix[TOP][c] = list(q)[i]
                i += 1
            TOP += 1
            for r in range(TOP, BOTTOM + 1):
                matrix[r][RIGHT] = list(q)[i]
                i += 1
            RIGHT -= 1
            for c in range(RIGHT, LEFT - 1, -1):
                matrix[BOTTOM][c] = list(q)[i]
                i += 1
            BOTTOM -= 1
            for r in range(BOTTOM, TOP - 1, -1):
                matrix[r][LEFT] = list(q)[i]
                i += 1
            LEFT += 1
                