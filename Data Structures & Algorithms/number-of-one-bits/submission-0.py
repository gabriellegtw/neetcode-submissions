class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for num in bin(n):
            if num == '1':
                res += 1

        return res
        