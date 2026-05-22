class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p2 >= 0:
            num1 = nums1[p1] if p1 >= 0 else float('-inf')
            num2 = nums2[p2] if p2 >= 0 else float('-inf')
            if num2 > num1:
                nums1[p] = num2
                p2 -= 1
            else:
                nums1[p] = num1
                p1 -= 1
            p -= 1



        