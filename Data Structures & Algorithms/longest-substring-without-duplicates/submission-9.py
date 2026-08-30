class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        l = 0
        r = 0
        result = 0

        while (r < len(s)):
            left = s[l]
            right = s[r]

            hash[right] = hash.get(right, 0) + 1

            while 2 in hash.values():
                # Remove left element from hashmap
                hash[left] = hash.get(left, 0) - 1
                l += 1
                left = s[l]

            result = max(result, r - l + 1)
            r += 1

        return result

        