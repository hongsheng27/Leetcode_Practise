class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        freq = Counter(hand)
        hand.sort()
        p = 0
        while p < len(hand):
            freq[hand[p]] -= 1
            for i in range(1, groupSize):
                if freq[hand[p] + i]:
                    freq[hand[p] + i] -= 1
                else: return False
            p += 1
            while p < len(hand) and not freq[hand[p]]:
                p += 1
        return True

