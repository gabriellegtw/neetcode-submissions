class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        count = 1
        l = 0
        r = 1
        d[s[l]] = 1

        while r < len(s) and l <= r:
            if d.get(s[r]) == None:
                d[s[r]] = 1
            else:
                d[s[r]] += 1

            if sum(d.values()) - max(d.values()) <= k:
                count = max(count, sum(d.values()))
            else:
                while sum(d.values()) - max(d.values()) > k:
                    d[s[l]] -= 1
                    l = l + 1

                count = max(count, sum(d.values()))

            r = r + 1

        return count

        