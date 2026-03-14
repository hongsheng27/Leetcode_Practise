class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        rightmostIndex = [-1] * len(nums2)

        for i, n in enumerate(nums2):
            while stack and stack[-1][1] < n:
                index, number = stack.pop()
                rightmostIndex[index] = n
            stack.append((i, n))

        ans = []
        for n in nums1:
            for i, n2 in enumerate(nums2):
                if n == n2:
                    ans.append(rightmostIndex[i])
        return ans




