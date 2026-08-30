class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        l = 0
        r = 1

        count = 1

        res = set()
        res.add(s[l])

        while r < len(s) and l <= r:
            if s[r] not in res:
                res.add(s[r])
                r = r + 1
                count = max(count, len(res))
            else:
                while s[r] in res:
                    res.remove(s[l])
                    l = l + 1

                res.add(s[r])
                r = r + 1
                count = max(count, len(res))

        return count


        
        