class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            curr = nums[i]
            # Intially put this as l = 0
            # But the brute force method is to do three loops
            # where l is always more than i
            l = i + 1
            r = len(nums) - 1

            while l < r:

                if l == i:
                    l += 1
                    continue
                if r == i:
                    r -= 1
                    continue
                
                if nums[l] + nums[r] + nums[i] == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    l += 1

        return res

                