class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # base case
        if rowIndex == 0: return [1]

        child = self.getRow(rowIndex - 1)
        row = [1]
        for i in range(len(child) - 1):
            row += [child[i] + child[i + 1]]
        row += [1]
        return row

