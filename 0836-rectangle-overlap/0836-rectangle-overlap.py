class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # choose bigger retangle
        # if one of small retangel's corner incide the big retangle, return true
        # if rec1 == rec2: return True
        # rec1Area = (rec1[1] - rec1[0]) * (rec1[3] - rec1[2])
        # rec2Area = (rec2[1] - rec2[0]) * (rec2[3] - rec2[2])
        # big = small = None
        # if rec1Area >= rec2Area:
        #     # equal
        #     big = rec1
        #     small = rec2
        # else:
        #     big = rec2
        #     small = rec1
        # cornners = ((0, 1), (2, 3), (2, 1), (0, 3))
         
        # for conner in cornners:
        #     if big[0] < conner[0] < big[2] and big[1] < conner[1] < big[3]:
        #         return True
        # return False
        # (33: 46)
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
        print(isXOverlap, isYOverlap)
      
        return isXOverlap and isYOverlap

        
        
