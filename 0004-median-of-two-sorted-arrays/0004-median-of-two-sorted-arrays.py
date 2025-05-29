class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # a
            j = half - i - 2 # b

            leftA = A[i] if i >= 0 else float('-inf')
            leftB = B[j] if j >= 0 else float('-inf')
            rightA = A[i + 1] if (i + 1) < len(A) else float('inf')
            rightB = B[j + 1] if (j + 1) < len(B) else float('inf')
            
            if leftA <= rightB and leftB <= rightA:
                # odd
                if total % 2:
                    return min(rightA, rightB)
                return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                r = i - 1
            else:
                l = i + 1
        