class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = 0
        for i, r in enumerate(matrix):
            if target <= r[-1]:
                index = i
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