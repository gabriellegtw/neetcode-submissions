class Solution:
    def maxScore(self, s: str) -> int:
        res = 0

        left = 0
        right = 0

        if s[0] == "0":
            left = 1

        for char in s[1:]:
            if char == "1":
                right += 1

        res = left + right
        curr = s[1:]
        while len(curr) > 1:
            if curr[0] == "1":
                right -= 1
            else:
                left += 1

            res = max(res, left + right)

            curr = curr[1:]
            
        return res

        