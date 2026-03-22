class TicTacToe:
    def __init__(self, n: int):
        self.h = [0] * n
        self.v = [0] * n
        self.d = 0
        self.rd = 0
    def move(self, row: int, col: int, player: int) -> int:
        number = 1 if player == 1 else -1
        n = len(self.h)
        self.h[row] += number 
        self.v[col] += number
        if row - col == 0:
            self.d += number
        if row + col == n - 1:
            self.rd += number
        if abs(self.h[row]) == n or abs(self.v[col]) == n or abs(self.d) == n or abs(self.rd) == n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)