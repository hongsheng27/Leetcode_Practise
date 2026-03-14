class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater = [-1] * len(nums2)
        count = {}
        ans = []

        for i, n in enumerate(nums2):
            count[n] = i

        for i, n in enumerate(nums2):
            while stack and stack[-1][1] < n:
                index, number = stack.pop()
                greater[index] = n
            stack.append((i, n))

        for n in nums1:
            index = count[n]
            ans.append(greater[index])
        return ans




