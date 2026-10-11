class Number:
    def __init__(self, num):
        self.num = str(num)
    def __lt__(self, other):
        return self.num + other.num > other.num + self.num 

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = [Number(num) for num in nums]
        nums.sort()
        
        if nums[0].num == "0":
            return "0"
        return "".join(num.num for num in nums)
        


        