class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = [-1] * len(nums2)
        stack = []
        for i, n in enumerate(nums2):
            while stack and stack[-1][1] < n:
                index, _ = stack.pop()
                nextGreater[index] = n
            stack.append((i, n))
        return [nextGreater[nums2.index(n)] for n in nums1]