class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        _product = 1
        _sum = 0
        while n:
            digit = n % 10 
            n = n // 10 

            _product *= digit
            _sum += digit
        return _product - _sum



