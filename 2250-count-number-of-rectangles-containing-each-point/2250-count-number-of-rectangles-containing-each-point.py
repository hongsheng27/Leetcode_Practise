class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        bucket = [[] for _ in range(101)] # keep zero
        # O(R)
        for l, h in rectangles:
            bucket[h].append(l)
        # 100 * log R
        for h in range(1, 101):
            bucket[h].sort()
        # O(P)
        res = []
        for x, y in points:
            arr = bucket[y:]
            total = 0
            for lst in arr: 
                l = 0
                r = len(lst)

                while l < r:
                    m = (l + r) // 2
                    if lst[m] < x:
                        l = m + 1
                    else:
                        r = m
                total += (len(lst) - l)
            res.append(total)
        return res