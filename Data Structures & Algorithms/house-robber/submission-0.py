class Solution:
    def rob(self, nums: List[int]) -> int:
        # For DP problem, come up the the "recursive" thought
        # Do this by thinking of one step on its own
        # In this example, dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        # At each step, the optimal solution is the larger between
        # the current results up to the previous house or the current house plus the optimal result 2 houses ago

        for i in range(len(nums)):
            prev = 0
            if i - 1 >= 0:
                prev = nums[i - 1]
            
            two_ago = 0
            if i - 2 >= 0:
                two_ago = nums[i - 2]

            nums[i] = max(prev, nums[i] + two_ago)

        return nums[-1]
        