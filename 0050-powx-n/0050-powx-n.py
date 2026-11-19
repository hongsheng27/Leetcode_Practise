class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursion(base, exp, total):
            if exp == 0:
                return total

            if exp % 2 == 1:
                total *= base

            return recursion(base ** 2, exp // 2, total)

        if n >= 0:
            return recursion(x, n, 1.0)

        if abs(x) > 1:
            return recursion(1 / x, -n, 1.0)

        return 1 / recursion(x, -n, 1.0)