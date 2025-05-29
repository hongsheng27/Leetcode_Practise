class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        p1 , p2 = 0, 0
        nums3 = []
        
        while p1 <= m - 1 or p2 <= n - 1:
            if p1 > m - 1:
                nums3.append(nums2[p2])
                p2 += 1
            elif p2 > n - 1:
                nums3.append(nums1[p1])
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                nums3.append(nums2[p2])
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                nums3.append(nums1[p1])
                p1 += 1
            else:
                nums3.append(nums1[p1])
                nums3.append(nums2[p2])
                p1 += 1
                p2 += 1

        l, r = 0, len(nums3) - 1 
        m = (l + r) // 2
        if len(nums3) % 2 == 0:
            return (nums3[m] + nums3[m + 1]) / 2
        else:
            return nums3[m]


        return ''
            
        

