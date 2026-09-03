class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
            
        arr1 = nums[1:]
        arr2 = nums[:-1]

        for i in range(len(arr1)):
            prev1 = 0
            prev2 = 0
            if i - 1 >= 0:
                prev1 = arr1[i - 1]
                prev2 = arr2[i - 1]
            
            two_ago1 = 0
            two_ago2 = 0
            if i - 2 >= 0:
                two_ago1 = arr1[i - 2]
                two_ago2 = arr2[i - 2]

            arr1[i] = max(prev1, arr1[i] + two_ago1)
            arr2[i] = max(prev2, arr2[i] + two_ago2)

        return max(arr1[-1], arr2[-1])