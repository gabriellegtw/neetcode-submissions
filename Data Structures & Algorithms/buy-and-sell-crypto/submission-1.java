class Solution {
    public int maxProfit(int[] prices) {
        int maxSum = Integer.MIN_VALUE;

        for (int l = 0; l < prices.length; l++) {
            for (int r = l; r < prices.length; r++) {
                maxSum = Math.max(maxSum, prices[r] - prices[l]);
            }
        }

        if (maxSum < 0) {
            return 0;
        }

        return maxSum;        
    }
}
