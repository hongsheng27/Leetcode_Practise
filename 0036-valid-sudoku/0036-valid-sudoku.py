class Solution(object):
    def isValidSudoku(self, board):
        for line in board:
            count = {}
            for c in line:
                if c == ".":
                    continue
                count[c] = 1 + count.get(c, 0)
                if count[c] > 1 : return False

        seen = {}
        for i in range(9):
            for line in board:
                if line[i] == '.':
                    continue
                seen[line[i]] = 1 + seen.get(line[i], 0)
                if seen[line[i]] > 1:
                    return False
            seen = {}

        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
    	        count = {}
                for i in range(3):
                    for j in range(3):
                        num = board[box_row+i][box_col+j]
                        if num != ".":
                            count[num] = 1 + count.get(num, 0)
                        if count.get(num) > 1:
                            return False
                print(count)
                count = {}
                    
        return True

        