class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        for index_1, c in enumerate(nums1):
            currentNums = float('inf')
            for index_2, j in enumerate(nums2):
                if c == j:
                    currentNums = j
                elif j > currentNums:
                    res[index_1] = j
                    break
        return res
