class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        while n:
            digit = n % 10 
            n //= 10 

            product *= digit
            total += digit
        return product - total



