class Solution(object):
    def isValidSudoku(self, board):
        # check row
        for row in board:
            seen = set()
            for val in row:
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)
  
        # check column
        for col in range(9):
            seen = set()
            for row in board:
                val = row[col]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        # check 3*3 box
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
    	        seen = set()
                for r in range(3):
                    for c in range(3):
                        val = board[box_row + r][box_col + c]
                        if val != ".":
                            if val in seen: 
                                return False
                            seen.add(val)     
        return True

        