class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = [str(num) for num in nums]
        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1
        nums.sort(key = cmp_to_key(compare))
        return str(int("".join(nums)))



        