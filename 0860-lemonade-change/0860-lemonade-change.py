class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        wallets = [0, 0] # [$5, $10]
        for bill in bills:
            if bill == 5:
                wallets[0] += 1
            elif bill == 10:
                wallets[0] -= 1
                wallets[1] += 1
            else:
                if wallets[1] and wallets[0]:
                    wallets[0] -= 1
                    wallets[1] -= 1
                else:
                    wallets[0] -= 3
            if wallets[0] < 0 or wallets[1] < 0: return False
        return True
            
        