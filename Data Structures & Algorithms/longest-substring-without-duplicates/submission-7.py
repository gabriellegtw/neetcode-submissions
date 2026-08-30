class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # I did this myself!!
        visited = set()

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        l = 0
        r = 1

        res = 0

        visited.add(s[l])

        while l < len(s) and r < len(s):
            if s[r] not in visited:
                visited.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else:
                while l < r and s[r] in visited:
                    visited.remove(s[l])
                    l += 1
                visited.add(s[r])
                res = max(res, r - l + 1)
                r += 1

        return res

