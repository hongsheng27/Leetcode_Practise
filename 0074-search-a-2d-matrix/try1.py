class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new_lst = []
        for lst in matrix:
            new_lst += lst
        
        left, right = 0, len(new_lst) - 1

        while left <= right:
            middle = (right + left) // 2
            if new_lst[middle] < target:
                left = middle + 1
            elif new_lst[middle] > target:
                right = middle - 1
            else:
                return True
        return False