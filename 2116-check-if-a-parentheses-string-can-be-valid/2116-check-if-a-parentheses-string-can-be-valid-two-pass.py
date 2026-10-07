class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2: return False
        balance = 0
        for i in range(len(s)):
            if locked[i] == '0' or s[i] == "(":
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        balance = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return True
        