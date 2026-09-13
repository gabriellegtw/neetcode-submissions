class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        r = minutes

        res = 0

        while r <= len(customers):
            sat = 0
            for i in range(len(customers)):
                if i >= l and i < r:
                    sat += customers[i]

                if grumpy[i] == 0 and (i < l or i >= r):
                    sat += customers[i]

            l += 1
            r += 1

            res = max(res, sat)

        return res
        