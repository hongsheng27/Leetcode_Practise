class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # base case
        if rowIndex == 0: return [1]

        prev_row = self.getRow(rowIndex - 1)
        row = [1]
        for i in range(len(prev_row) - 1):
            row += [prev_row[i] + prev_row[i + 1]]
        row += [1]
        return row

