class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
            
        nums.sort()
        count = 0
        curr = 0

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                curr = curr + 1
                count = max(count, curr)
            elif nums[i + 1] == nums[i]:
                continue
            else:
                curr = 0
        
        return count + 1
        