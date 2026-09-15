class Solution:
    def compress(self, chars: List[str]) -> int:
        l = tail = 0
        for r in range(len(chars)):
            if r + 1 < len(chars) and chars[r] != chars[r + 1] or r == len(chars) - 1:
                length = r - l + 1
                l = r + 1
                chars[tail] = chars[r]
                tail += 1
                if length == 1:
                    continue
                elif length < 10:
                    chars[tail] = str(length)
                    tail += 1
                else:
                    for i in str(length):
                        chars[tail] = i
                        tail += 1
        chars = chars[:tail]
        return len(chars)