class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        i = j = 0
        cur = prev = 0
        for _ in range((m + n) // 2 + 1):
            prev = cur
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                cur = nums1[i]
                i += 1
            else:
                cur = nums2[j]
                j += 1
        if (m + n) % 2:
            return cur
        return (prev + cur) / 2