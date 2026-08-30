class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        result = nums[0]
        while (l <= r):
            mid = int((l + r) / 2)
            result = min(nums[mid], result)
            if nums[mid] < nums[r]:
                # search left
                r = mid
            else:
                # search right
                l = mid + 1

        return result
        