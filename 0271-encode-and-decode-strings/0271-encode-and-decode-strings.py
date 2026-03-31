class Codec:
    def encode(self, strs: List[str]) -> str:
        newList = []
        for s in strs:
            newList.append(str(len(s)) + "#" + s)
        return "".join(newList)

    def decode(self, s: str) -> List[str]:
        l = 0
        res = []
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l = r + 1
            res.append(s[l:l + length])
            l = l + length
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))