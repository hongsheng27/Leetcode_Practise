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
        upper = 2 ** 31 - 1
        lower = -2 ** 31
        def toNumber(ch):
            if ch in StringToInt:
                return StringToInt[ch]
            else:
                return None
        signed = 1
        res = 0

        for i, ch in enumerate(s.strip()):
            print(ch)
            if i == 0 and ch in ("-", "+") : 
                if ch == "-": signed = -1
                continue
            num = toNumber(ch)
            if num != None:
                res = res * 10 + num
            else:
                break
        res = res * signed
        if res > upper:
                res = upper
        elif res < lower:
            res = lower
        return res
