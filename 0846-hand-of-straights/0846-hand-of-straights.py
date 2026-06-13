class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        count = Counter(hand)
        for num in hand:
            if count[num] == 0: continue
            for i in range(num, num + groupSize):
                count[i] -= 1
                if count[i] < 0: return False
        return True



        