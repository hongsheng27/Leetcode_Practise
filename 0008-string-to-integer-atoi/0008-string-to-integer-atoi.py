class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        sign = 1
        res = 0
        for i, ch in enumerate(s.strip()):
            if i == 0 and ch in "+-" : 
                if ch == "-": sign = -1
                continue
            if ch.isdigit():
                num = ord(ch) - ord('0')
                if res > (INT_MAX - num) // 10:
                    return INT_MAX if sign == 1 else INT_MIN
                res = res * 10 + num
            else:
                break
        res = res * sign
        
        return res
