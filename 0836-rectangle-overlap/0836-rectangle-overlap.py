class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        isXoverlap = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])
        isYoverplap = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
        return isXoverlap and isYoverplap
