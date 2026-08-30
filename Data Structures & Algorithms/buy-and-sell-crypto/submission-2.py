class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1

        while r < len(prices) and l < r:
            curr = prices[r] - prices[l]
            profit = max(profit, curr)
            if curr <= 0:
                l = r
                r = l + 1
            else:
                r = r + 1

        return profit
        