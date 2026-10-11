class Number:
    def __init__(self, num):
        self.num = str(num)
    def __lt__(self, other):
        return self.num + other.num > other.num + self.num 

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = [Number(num) for num in nums]
        nums.sort(key = lambda x: x)
        res = []
        for n in nums:
            res.append(n.num)
        
        return str(int("".join(res)))
        


        