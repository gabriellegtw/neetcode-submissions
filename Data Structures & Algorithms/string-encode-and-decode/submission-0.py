class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res = res + str(len(i)) + "#" + i
        return res



    def decode(self, s: str) -> List[str]:
        w = len(s)
        res = []
        l = 0
        r = 1
        while l < w and r < w + 1:
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            res.append(s[l:r])
            l = r

        return res


