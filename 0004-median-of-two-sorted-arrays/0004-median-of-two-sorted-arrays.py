class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)

        l = 0
        r = n

        while l <= r:
            i = (l + r) // 2
            j = (m + n + 1) // 2 - i

            nums1Left = nums1[i - 1] if i > 0 else float('-inf')
            nums1Right = nums1[i] if i < n else float('inf')
            nums2Left = nums2[j - 1] if j > 0 else float('-inf')
            nums2Right = nums2[j] if j < m else float('inf')

            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if not (m + n) % 2:
                    return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
                return max(nums1Left, nums2Left)
            elif nums1Left > nums2Right:
                r = i - 1
            else:
                l = i + 1

        
