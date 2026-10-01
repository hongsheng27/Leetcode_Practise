class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and stack[-1] > n and k:
                stack.pop()
                k -= 1
            stack.append(n)
        while k > 0:
            stack.pop()
            k -= 1
        res = "".join(stack).lstrip("0")
        return "0" if not res else res
        
        


        
            

