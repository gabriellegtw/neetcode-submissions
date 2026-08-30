class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash = {}
        result = 0
        if len(s) <= 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            l = 0
            r = 0

            while (r < len(s)):
                hash[s[r]] = hash.get(s[r], 0) + 1
                toChange = r - l + 1 - max(hash.values())

                while (toChange > k):
                    hash[s[l]] = max(hash.get(s[l], 0) - 1, 0)
                    l += 1
                    toChange = r - l + 1 - max(hash.values())

                result = max(result, r - l + 1)
                r += 1

            return result 
        