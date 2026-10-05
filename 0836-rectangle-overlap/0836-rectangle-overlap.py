class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # solution1 (not work): choose bigger retangle
        # if one of small retangel's corner incide the big retangle, return true
        # if rec1 == rec2: return True
      
        # solution2 : find if x axios overlap, start from rec[0] is smaller
        # find if y axios overlap, start from rec[1] is smaller
        isXOverlap = False
        isYOverlap = False
        if rec1[0] >= rec2[0]:
            rec1, rec2 = rec2, rec1
        if rec2[0] < rec1[2]:
            isXOverlap = True

        if rec1[1] >= rec2[1]:
            rec1, rec2 = rec2, rec1
        if rec2[1] < rec1[3]:
            isYOverlap = True
      
        return isXOverlap and isYOverlap
        # (54:09 done)

        
        
