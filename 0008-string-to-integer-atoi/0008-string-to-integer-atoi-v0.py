class Solution:
    def myAtoi(self, s: str) -> int:
        StringToInt = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0
        }
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        def toNumber(ch):
            if ch in StringToInt:
                return StringToInt[ch]
            else:
                return None

        sign = 1
        res = 0
        for i, ch in enumerate(s.strip()):
            if i == 0 and ch in "+-" : 
                if ch == "-": sign = -1
                continue
            num = toNumber(ch)
            if num != None:
                if res > (INT_MAX - num) // 10:
                    return INT_MAX if sign == 1 else INT_MIN
                res = res * 10 + num
            else:
                break
        res = res * sign
        
        return res
