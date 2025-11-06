class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]
       
        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                box_index = (row_index // 3) * 3 + col_index // 3
                if col == '.': continue
                if (col not in rows[row_index]) and (col not in cols[col_index]) and (col not in boxs[box_index]): 
                    rows[row_index].add(col)
                    cols[col_index].add(col)
                    boxs[box_index].add(col)
                else:
                    return False
        return True
                

      
    