class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        TOP = LEFT = 0
        BOTTOM = RIGHT = len(matrix) - 1
        
        while TOP < BOTTOM and LEFT < RIGHT:
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
            
            for c in range(LEFT, RIGHT + 1):
                matrix[TOP][c] = q.popleft()
            for r in range(TOP + 1, BOTTOM + 1):
                matrix[r][RIGHT] = q.popleft()
            for c in range(RIGHT - 1, LEFT - 1, -1):
                matrix[BOTTOM][c] = q.popleft()
            for r in range(BOTTOM - 1, TOP, -1):
                matrix[r][LEFT] = q.popleft()
            
            TOP += 1
            RIGHT -= 1
            BOTTOM -= 1
            LEFT += 1