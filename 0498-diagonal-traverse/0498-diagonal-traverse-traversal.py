class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])
        d = ROWS + COLS - 1
        res = []
        for _d in range(d):
            if not _d % 2: 
                startR = min(_d, ROWS - 1) 
                startC = _d - startR
                res.append(mat[startR][startC])
                # even
                dr, dc = -1, 1

            else:
                startC = min(_d, COLS - 1) 
                startR = _d - startC
                res.append(mat[startR][startC])
                # odd
                dr, dc = 1, -1
                
            nr, nc = startR + dr, startC + dc
            while 0 <= nr < ROWS and 0 <= nc < COLS:
                res.append(mat[nr][nc])
                nr += dr
                nc += dc
        return res
        

            

    