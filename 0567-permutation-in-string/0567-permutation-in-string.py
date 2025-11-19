class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        count1, count2 = {}, {}
        for c in s1:
            count1[c] = count1.get(c, 0) + 1
        
        k = len(s1)

        for i, c in enumerate(s2):
            count2[c] = count2.get(c, 0) + 1

            if i >= k:
                left_char = s2[i - k]
                count2[left_char] -= 1
                if count2[left_char] == 0:
                    del count2[left_char]
            if count1 == count2:
                return True
        return False