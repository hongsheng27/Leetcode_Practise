class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # need return list of row
        # each row can generate by previous one, traverse from 0 - numRows
        # i.g. i = 3, [1, 2, 1] => [1, 3, 3, 1], to get i = 3 row, I need to traverse i = 2 row
        # complecity will be 1 + 2 + 3 + ..n = n (n + 1) / 2 O(n ^ 2)
        res = [[1]]
        for _ in range(numRows - 1):
            level = [1]
            if len(res[-1]) > 1:
                for j in range(len(res[-1])):
                    if j + 1 < len(res[-1]):
                        level += [res[-1][j] + res[-1][j + 1]]
            level += [1]
            res.append(level)
        return res
        