class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreater = {} # {num2: nextGreaterNums2}
        for n in nums2:
            while stack and stack[-1] < n:
                num2 = stack.pop()
                nextGreater[num2] = n
            stack.append(n)
        return [nextGreater.get(num1, -1) for num1 in nums1]
        



        