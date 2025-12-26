class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        freq = Counter(hand)
        hand.sort()
        for num in hand:
            if not freq[num]: continue
            for i in range(num, num + groupSize):
                if freq[i]:
                    freq[i] -= 1
                else: return False
        return True

