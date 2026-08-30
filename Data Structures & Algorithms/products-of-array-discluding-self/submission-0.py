class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            num = 1
            for j in range(0, len(nums)):
                if i == j:
                    continue
                num *= nums[j]
            res.append(num)

        return res
                

        