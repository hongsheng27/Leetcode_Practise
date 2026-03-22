class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.h = [0] * n
        self.v = [0] * n
        self.d = 0
        self.ad = 0
    def move(self, row: int, col: int, player: int) -> int:
        score = 1 if player == 1 else -1
        self.h[row] += score 
        self.v[col] += score
        if row - col == 0:
            self.d += score
        if row + col == self.n - 1:
            self.ad += score
        if abs(self.h[row]) == self.n or abs(self.v[col]) == self.n or abs(self.d) == self.n or abs(self.ad) == self.n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)