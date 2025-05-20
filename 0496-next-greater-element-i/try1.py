class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0] * len(nums1)
        greater = [-1] * len(nums2)
        stack = []

        count = {}
        for i, c in enumerate(nums2):
            count[c] = i

        for i, n in enumerate(nums2):
            while stack and n > stack[-1][1]:
                pop_i, pop_n = stack.pop()
                greater[pop_i] = n
            stack.append([i,n])

        for i, c in enumerate(nums1):
            greater_index = count[c]
            res[i] = greater[greater_index]

        return res
