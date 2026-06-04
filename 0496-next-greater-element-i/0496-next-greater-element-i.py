class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2Index = {}
        for i, num2 in enumerate(nums2):
            nums2Index[num2] = i
        nextGreaterList = [-1] * len(nums2)
        stack = []
        for i in range(len(nums2)):
            while stack and stack[-1][1] < nums2[i]:
                index, value = stack.pop()
                nextGreaterList[index] = nums2[i]
            stack.append((i, nums2[i]))
        res = []
        for num1 in nums1:
            index = nums2Index[num1]
            res.append(nextGreaterList[index])
        return res