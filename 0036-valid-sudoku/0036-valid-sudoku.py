class Solution(object):
    def isValidSudoku(self, board):
        for line in board:
            count = {}
            for c in line:
                if c == ".":
                    continue
                count[c] = 1 + count.get(c, 0)
                if count[c] > 1 : return False

        for i in range(9):
            count = {}
            for line in board:
                if line[i] != '.':
                    count[line[i]] = 1 + count.get(line[i], 0)
                if count.get(line[i]) > 1:
                    return False

        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
    	        count = {}
                for r in range(3):
                    for c in range(3):
                        num = board[box_row + r][box_col + c]
                        if num != ".":
                            count[num] = 1 + count.get(num, 0)
                        if count.get(num) > 1:
                            return False
                count = {}
                    
        return True

        