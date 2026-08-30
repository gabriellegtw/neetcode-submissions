class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = int((l + r) / 2)

            if nums[mid] == target:
                return mid

            if nums[l] == target:
                return l

            if nums[r] == target:
                return r

            # If the right side is sorted
            if nums[mid] < nums[r]:
                # if out of range
                if target > nums[r] or target < nums[mid]:
                    # shift to left
                    r = mid - 1
                else: 
                    l = mid + 1
            else:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
        