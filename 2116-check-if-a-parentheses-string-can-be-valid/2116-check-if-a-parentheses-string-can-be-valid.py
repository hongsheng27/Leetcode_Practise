class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        openStack = []
        free = []
        for i in range(len(s)):
            if locked[i] == "1":
                if s[i] == "(":
                    openStack.append(i)
                else:
                    if openStack:
                        openStack.pop()
                    elif free:
                        free.pop()
                    else:
                        return False
            else:
                free.append(i)
        while openStack and free:
            if openStack[-1] < free[-1]:
                openStack.pop()
                free.pop()
            else:
                return False
        if len(openStack): return False
        return len(free) % 2 == 0
        
       
