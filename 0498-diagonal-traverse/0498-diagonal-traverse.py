class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])
        buckets = [[] for _ in range(ROWS + COLS - 1)]
        for r in range(ROWS):
            for c in range(COLS):
                buckets[r + c].append(mat[r][c])
        res = []
        for d, bucket in enumerate(buckets):
            res.extend(list(reversed(bucket)) if d % 2 == 0 else bucket)
        return res
        
        