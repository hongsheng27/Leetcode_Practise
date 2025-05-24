class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = 0

        left, right = 0, len(matrix) - 1
        while left < right:
            middle = (right + left) // 2
            if matrix[middle][-1] < target:
                if right - left == 1:
                    index = left + 1
                    break
                left = middle
            elif matrix[middle][-1] > target:
                if right - left == 1:
                    index = left
                    break
                right = middle
            else:
                index = middle
                break

           
        new_lst = matrix[index]

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