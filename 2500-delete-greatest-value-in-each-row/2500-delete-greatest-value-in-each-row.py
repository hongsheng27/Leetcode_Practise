class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        res = 0
        sortGrid = []
        for g in grid:
            sortGrid.append(sorted(g))
        for _ in range(len(grid[0])):
            maxValue = float('-inf')
            for g in sortGrid:
                elem = g.pop()
                maxValue = max(maxValue, elem)
            res += maxValue
        return res
