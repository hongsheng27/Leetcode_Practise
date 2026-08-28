class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        buckets = [[] for _ in range(101)]
        for x, y in rectangles:
            buckets[y].append(x)
        for bucket in buckets:
            bucket.sort()
        res = []
        for x, y in points:
            total = 0
            for bucket in buckets[y:]:
                l = 0
                r = len(bucket)
                while l < r:
                    m = (l + r) // 2
                    if bucket[m] < x:
                        l = m + 1
                    else:
                        r = m
                total += len(bucket) - l
            res.append(total)
        return res